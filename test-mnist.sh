mkdir mnist-ortho-1
python run-aec-mnist.py \
  --dimension 100 200 \
  --alpha 0.04 \
  --beta 0. \
  --gamma 0. \
  --sigma 0.1 \
  --noise 0.1 \
  --npoints 100 \
  --weights 0.14 \
  --stochastic 0 \
  --factor 1 \
  --frate 0 \
  --lrate 0.00001 \
  --inner 1000 \
  --outer 20 \
  --file './mnist-ortho-1'




