from pykeen.pipeline import pipeline

result = pipeline(
    model='NTN',
    dataset='nations',
    model_kwargs=dict(num_slices=1)
)