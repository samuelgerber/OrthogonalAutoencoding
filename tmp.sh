

mkdir tmp 
python run-aec-sine.py \
  --dimension 50 100  200 100 50 \
  --alpha 1. \
  --tortho "" \
  --beta 10000. \
  --gamma 1 \
  --sigma 0. \
  --noise 0.1 \
  --npoints 100 \
  --weights 0.15 \
  --stochastic 0 \
  --factor 0.0001 \
  --frate 0.0001 \
  --lrate 0.00001 \
  --inner 200 \
  --outer 100 \
  --file "./tmp"



