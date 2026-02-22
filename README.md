# AI-Powered Medical Diagnosis Assistant

This project is to build a modular AI medical assistant that transforms symptom descriptions into research-backed insights. The system combines LLM reasoning with real-time PubMed retrieval and exposes it as both a REST API and MCP tool for agent workflows..

## Project Description 

This project is an intelligent medical assistance platform that transforms free-text symptom descriptions into structured, research-backed insights. The system analyzes user-provided symptoms, generates potential diagnoses using Azure OpenAI models, retrieves relevant biomedical literature from PubMed, and summarizes complex medical abstracts into concise, easy-to-understand outputs.

The application is designed with a modular architecture and is accessible through:

A RESTful API built with FastAPI

A custom tool implemented using FastMCP (Model Context Protocol) for AI agent integration

This project demonstrates practical experience in LLM orchestration, external API integration, and agent-compatible AI system design.

## Tech Stack & Frameworks

LLM: Azure OpenAI (GPT model / Chat Completion API)

Backend Framework: FastAPI

Protocol Integration: FastMCP (Model Context Protocol)

Research Data Source: PubMed E-utilities API

Parsing: BeautifulSoup (XML parsing)

Validation: Pydantic

Language: Python

## Key Highlights

* Designed modular AI pipeline: Extraction → Diagnosis → Research Retrieval → Summarization

* Integrated LLMs with real-time biomedical research data

* Built reusable MCP tool for AI agent integration

* Implemented error handling and fallback mechanisms for API reliability

* This project showcases practical experience in building production-style AI systems that combine language models with external knowledge sources and agent-compatible architectures.
