mkdir penalty-contraction-1
python run-aec-sine.py \
  --dimension 50 50\
  --alpha 0. \
  --beta 0.04 \
  --gamma 0. \
  --sigma 0. \
  --noise 0.1 \
  --npoints 100 \
  --weights 0.14 \
  --stochastic 0 \
  --factor 1 \
  --frate 0 \
  --lrate 0.00001 \
  --inner 200 \
  --outer 100 \
  --file './penalty-contraction-1'


mkdir penalty-contraction-2
python run-aec-sine.py \
  --dimension 50 50\
  --alpha 0. \
  --beta 0.02 \
  --gamma 0. \
  --sigma 0. \
  --noise 0.1 \
  --npoints 100 \
  --weights 0.14 \
  --stochastic 0 \
  --factor 1 \
  --frate 0 \
  --lrate 0.00001 \
  --inner 200 \
  --outer 100 \
  --file './penalty-contraction-2'

mkdir penalty-contraction-3
python run-aec-sine.py \
  --dimension 50 50\
  --alpha 0. \
  --beta 0.005 \
  --gamma 0. \
  --sigma 0. \
  --noise 0.1 \
  --npoints 100 \
  --weights 0.14 \
  --stochastic 0 \
  --factor 1 \
  --frate 0 \
  --lrate 0.00001 \
  --inner 200 \
  --outer 100 \
  --file './penalty-contraction-3'

