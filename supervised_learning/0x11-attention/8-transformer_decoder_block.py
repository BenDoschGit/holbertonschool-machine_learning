#!/usr/bin/env python3
"""Module that contains """

import tensorflow as tf
from tensorflow.keras.layers import Layer, Dense, LayerNormalization, Dropout
MultiHeadAttention = __import__('6-multihead_attention').MultiHeadAttention


class DecoderBlock(Layer):
    """Class that"""

    def __init__(self, dm, h, hidden, drop_rate=0.1):
        """Class constructor that"""
        super().__init__()
        self.mha1 = MultiHeadAttention(dm, h)
        self.mha2 = MultiHeadAttention(dm, h)
        self.dense_hidden = Dense(hidden, activation='relu')
        self.dense_output = Dense(dm)
        self.layernorm1 = LayerNormalization(epsilon=1e-6)
        self.layernorm2 = LayerNormalization(epsilon=1e-6)
        self.layernorm3 = LayerNormalization(epsilon=1e-6)
        self.dropout1 = Dropout(drop_rate)
        self.dropout2 = Dropout(drop_rate)
        self.dropout3 = Dropout(drop_rate)

    def call(self, x, encoder_output, training, look_ahead_mask, padding_mask):
        """Public instance method that"""

        # Output MHA block
        attention_output_1, _ = self.mha1(x, x, x, look_ahead_mask)
        dropout_output_1 = self.dropout1(attention_output_1, training=training)

        norm_output_1 = self.layernorm1(dropout_output_1 + x)

        # Input MHA block
        attention_output_2, _ = self.mha2(norm_output_1, encoder_output,
                                         encoder_output, padding_mask)
        dropout_output_2 = self.dropout2(attention_output_2, training=training)

        norm_output_2 = self.layernorm2(dropout_output_2 + norm_output_1)

        # Feed Forward Block
        dense_output_1 = self.dense_hidden(norm_output_2)
        dense_output_2 = self.dense_output(dense_output_1)
        dropout_output_3 = self.dropout3(dense_output_2, training=training)
        
        norm_output_3 = self.layernorm3(dropout_output_3 + norm_output_2)

        return norm_output_3
