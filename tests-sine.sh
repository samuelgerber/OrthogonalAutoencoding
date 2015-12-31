mkdir sine-contraction1
python run-aec-spiral.py \
  --dimension 50 100 200 200 100 50\
  --alpha 0. \
  --beta 0.1 \
  --gamma 0. \
  --sigma 0. \
  --noise 0.1 \
  --npoints 200 \
  --weights 0.14 \
  --stochastic 0 \
  --factor 1 \
  --frate 0 \
  --lrate 0.00001 \
  --inner 200 \
  --outer 100 \
  --file './sine-contraction1'
