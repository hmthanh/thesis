import torch

from models import SpKBGATModified, SpKBGATConvOnly
from torch.autograd import Variable
import torch.nn as nn
import torch.nn.functional as F
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
from copy import deepcopy

from preprocess import read_entity_from_id, read_relation_from_id, init_embeddings, build_data
from create_batch import Corpus
from utils import save_model

import random
import argparse
import os
import sys
import logging
import time
import pickle


class Args:
    # network arguments
    data = "./data/WN18RR/"
    epochs_gat = 3600
    epochs_conv = 200
    weight_decay_gat = float(5e-6)
    weight_decay_conv = float(1e-5)
    pretrained_emb = True
    embedding_size = 50
    lr = float(1e-3)
    get_2hop = True
    use_2hop = True
    partial_2hop = False
    output_folder = "./"

    # arguments for GAT
    batch_size_gat = 86835
    # Tỷ lệ của tập valid so với tập invalid trong khi training GAT
    valid_invalid_ratio_gat = 2
    drop_GAT = 0.3  # Tỷ lệ dropout của lớp SpGAT
    alpha = 0.2  # LeakyRelu alphs for SpGAT layer
    entity_out_dim = [100, 200]  # Miền nhúng của đầu ra output
    nheads_GAT = [2, 2]  # Multihead attention SpGAT
    # Margin used in hinge loss ( Sử dụng margin trong hinge (khớp nối))
    margin = 5

    # arguments for convolution network
    batch_size_conv = 128  # Batch size for conv
    alpha_conv = 0.2  # LeakyRelu alphas for conv layer
    # Ratio of valid to invalid triples for convolution training
    valid_invalid_ratio_conv = 40
    out_channels = 500  # Số lượng output channels trong lớp conv
    drop_conv = 0.0  # Xắc xuất dropout cho lớp convolution


args = Args()

entity_embeddings = torch.load("./data/WN18RR/entity_embeddings.pt")
relation_embeddings = torch.load("./data/WN18RR/relation_embeddings.pt")
Corpus_ = torch.load("./Corpus_torch.pt")

if(args.use_2hop):
    print("Opening node_neighbors pickle object")
    file = "./2hop.pickle"
    with open(file, 'rb') as handle:
        node_neighbors_2hop = pickle.load(handle)

entity_embeddings_copied = deepcopy(entity_embeddings)
relation_embeddings_copied = deepcopy(relation_embeddings)


CUDA = False #torch.cuda.is_available()
#
#
# print("Defining model")
#
# print(
#     "\nModel type -> GAT layer with {} heads used , Initital Embeddings training".format(args.nheads_GAT[0]))
# # SpKBGATModified : lớp GAT chính
# model_gat = SpKBGATModified(entity_embeddings, relation_embeddings, args.entity_out_dim, args.entity_out_dim,
#                             args.drop_GAT, args.alpha, args.nheads_GAT)
#
# if CUDA:
#     model_gat.cuda()
#
# optimizer = torch.optim.Adam(
#     model_gat.parameters(), lr=args.lr, weight_decay=args.weight_decay_gat)
#
# scheduler = torch.optim.lr_scheduler.StepLR(
#     optimizer, step_size=500, gamma=0.5, last_epoch=-1)
#
# gat_loss_func = nn.MarginRankingLoss(margin=args.margin)
#
# current_batch_2hop_indices = torch.tensor([])
# if(args.use_2hop):
#     current_batch_2hop_indices = Corpus_.get_batch_nhop_neighbors_all(args,
#                                                                       Corpus_.unique_entities_train, node_neighbors_2hop)
#
# if CUDA:
#     current_batch_2hop_indices = Variable(
#         torch.LongTensor(current_batch_2hop_indices)).cuda()
# else:
#     current_batch_2hop_indices = Variable(
#         torch.LongTensor(current_batch_2hop_indices))
#
# epoch_losses = []   # losses of all epochs
# print("Number of epochs {}".format(args.epochs_gat))
#
# epoch = 1
# ########################################################
# def batch_gat_loss(gat_loss_func, train_indices, entity_embed, relation_embed):
#     len_pos_triples = int(
#         train_indices.shape[0] / (int(args.valid_invalid_ratio_gat) + 1))
#
#     pos_triples = train_indices[:len_pos_triples]
#     neg_triples = train_indices[len_pos_triples:]
#
#     pos_triples = pos_triples.repeat(int(args.valid_invalid_ratio_gat), 1)
#
#     source_embeds = entity_embed[pos_triples[:, 0]]
#     relation_embeds = relation_embed[pos_triples[:, 1]]
#     tail_embeds = entity_embed[pos_triples[:, 2]]
#
#     x = source_embeds + relation_embeds - tail_embeds
#     pos_norm = torch.norm(x, p=1, dim=1)
#
#     source_embeds = entity_embed[neg_triples[:, 0]]
#     relation_embeds = relation_embed[neg_triples[:, 1]]
#     tail_embeds = entity_embed[neg_triples[:, 2]]
#
#     x = source_embeds + relation_embeds - tail_embeds
#     neg_norm = torch.norm(x, p=1, dim=1)
#
#     if (CUDA):
#         y = torch.ones(int(args.valid_invalid_ratio_gat) * len_pos_triples).cuda()
#     else:
#         y = torch.ones(int(args.valid_invalid_ratio_gat) * len_pos_triples)
#     loss = gat_loss_func(pos_norm, neg_norm, y)
#     return loss
# ############################################
#
#
# random.shuffle(Corpus_.train_triples)
# Corpus_.train_indices = np.array(
#     list(Corpus_.train_triples)).astype(np.int32)
#
# model_gat.train()  # getting in training mode
# start_time = time.time()
# epoch_loss = []
#
# if len(Corpus_.train_indices) % args.batch_size_gat == 0:
#     num_iters_per_epoch = len(
#         Corpus_.train_indices) // args.batch_size_gat
# else:
#     num_iters_per_epoch = (
#                                   len(Corpus_.train_indices) // args.batch_size_gat) + 1
#
# for iters in range(num_iters_per_epoch):
#     start_time_iter = time.time()
#     train_indices, train_values = Corpus_.get_iteration_batch(iters)
#
#     if CUDA:
#         train_indices = Variable(
#             torch.LongTensor(train_indices)).cuda()
#         train_values = Variable(torch.FloatTensor(train_values)).cuda()
#
#     else:
#         train_indices = Variable(torch.LongTensor(train_indices))
#         train_values = Variable(torch.FloatTensor(train_values))
#
#     # forward pass
#     entity_embed, relation_embed = model_gat(
#         Corpus_, Corpus_.train_adj_matrix, train_indices, current_batch_2hop_indices)
#
#     optimizer.zero_grad()
#
#     loss = batch_gat_loss(
#         gat_loss_func, train_indices, entity_embed, relation_embed)
#
#     loss.backward()
#     optimizer.step()
#
#     epoch_loss.append(loss.data.item())
#
#     end_time_iter = time.time()
#
#     print("Iteration-> {0}  , Iteration_time-> {1:.4f} , Iteration_loss {2:.4f}".format(
#         iters, end_time_iter - start_time_iter, loss.data.item()))
#
# scheduler.step()
# print("Epoch {} , average loss {} , epoch_time {}".format(
#     epoch, sum(epoch_loss) / len(epoch_loss), time.time() - start_time))
# epoch_losses.append(sum(epoch_loss) / len(epoch_loss))
#
# save_model(model_gat, args.data, epoch,
#            args.output_folder)
print("Defining model")
model_gat = SpKBGATModified(entity_embeddings, relation_embeddings, args.entity_out_dim, args.entity_out_dim,
                            args.drop_GAT, args.alpha, args.nheads_GAT)
print("Only Conv model trained")
model_conv = SpKBGATConvOnly(entity_embeddings, relation_embeddings, args.entity_out_dim, args.entity_out_dim,
                             args.drop_GAT, args.drop_conv, args.alpha, args.alpha_conv,
                             args.nheads_GAT, args.out_channels)

if CUDA:
    model_conv.cuda()
    model_gat.cuda()

model_gat.load_state_dict(torch.load(
    '{}/trained_{}.pth'.format("./gat/", args.epochs_gat - 1)), strict=False, map_location=torch.device('cpu'))
model_conv.final_entity_embeddings = model_gat.final_entity_embeddings
model_conv.final_relation_embeddings = model_gat.final_relation_embeddings

Corpus_.batch_size = args.batch_size_conv
Corpus_.invalid_valid_ratio = int(args.valid_invalid_ratio_conv)

optimizer = torch.optim.Adam(
    model_conv.parameters(), lr=args.lr, weight_decay=args.weight_decay_conv)

scheduler = torch.optim.lr_scheduler.StepLR(
    optimizer, step_size=25, gamma=0.5, last_epoch=-1)

margin_loss = torch.nn.SoftMarginLoss()


############################################
print("\nepoch-> ", 0)
random.shuffle(Corpus_.train_triples)
Corpus_.train_indices = np.array(
    list(Corpus_.train_triples)).astype(np.int32)

model_conv.train()  # getting in training mode
start_time = time.time()
epoch_loss = []

if len(Corpus_.train_indices) % args.batch_size_conv == 0:
    num_iters_per_epoch = len(
        Corpus_.train_indices) // args.batch_size_conv
else:
    num_iters_per_epoch = (
        len(Corpus_.train_indices) // args.batch_size_conv) + 1


train_indices, train_values = Corpus_.get_iteration_batch(0)

if CUDA:
    train_indices = Variable(
        torch.LongTensor(train_indices)).cuda()
    train_values = Variable(torch.FloatTensor(train_values)).cuda()

else:
    train_indices = Variable(torch.LongTensor(train_indices))
    train_values = Variable(torch.FloatTensor(train_values))

preds = model_conv(
    Corpus_, Corpus_.train_adj_matrix, train_indices)

