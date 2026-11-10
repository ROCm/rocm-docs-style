# Technical documentation review checklist

Items that surface during PR review, flagged for human judgment rather
than auto-correction.

## Competitor references

Flag mentions of NVIDIA, CUDA, or other NVIDIA-specific technologies (for
example, cuDNN, NCCL, NVLink, TensorRT). Do not state or imply that the
product supports or runs on NVIDIA GPUs. Vendor-agnostic wording is
acceptable when it is paired with a statement that the release is validated
on AMD GPUs. CUDA may remain when it is a literal identifier, device string,
environment variable, or package name. Do not enforce this with a Vale
existence check. A migration guide or compatibility table can name these
terms, and that still needs a human decision.
