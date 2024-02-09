# Vector Hybrid Search

- Create a Vector DB in Pinecone using Fashion datasets.
- Query through it.
- Adjust the 'Scaling Hybrid Search' to get optimize results.


## Sprase Vector encoding

To convert your own text corpus to sparse vectors, you can either use BM25 or SPLADE. This guide uses BM25, which is more common.

[Pinecone BM25](https://docs.pinecone.io/docs/encode-sparse-vectors)


## Upsert sparse-dense vectors

Pinecone supports vectors with sparse and dense values, which allows you to perform hybrid search, or semantic and keyword search, in one query and combine the results for more relevant results. This page explains the sparse-dense vector format and how to upsert sparse-dense vectors into Pinecone indexes.

[Pinecone Upsert](https://docs.pinecone.io/docs/encode-sparse-vectors](https://docs.pinecone.io/docs/upsert-sparse-dense-vectors)https://docs.pinecone.io/docs/upsert-sparse-dense-vectors)

## Query sparse-dense vectors

Because Pinecone views your sparse-dense vector as a single vector, it does not offer a built-in parameter to adjust the weight of a query's dense part against its sparse part; the index is agnostic to density or sparsity of coordinates in your vectors. You may, however, incorporate a linear weighting scheme by customizing your query vector.


[Pinecone Upsert](https://docs.pinecone.io/docs/query-sparse-dense-vectors)
