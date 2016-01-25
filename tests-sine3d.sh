mkdir tmp
python run-aec-sine3d.py \
  --dimension 50 100 200 200 100 50\
  --alpha 1. \
  --tortho ""\
  --beta 10 \
  --gamma 2. \
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
  --file './tmp'
