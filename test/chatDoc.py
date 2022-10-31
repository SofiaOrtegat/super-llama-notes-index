#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Env Variables
from dotenv import load_dotenv
load_dotenv()

from llama_index import (
    SimpleDirectoryReader,
    node_parser,
    VectorStoreIndex,
    ServiceContext
)

# configuring LLM
from llama_index.llm_predictor import HuggingFaceLLMPredictor
stable_ll