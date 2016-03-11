mkdir network-contraction-1
python run-aec-sine.py \
  --dimension 50 100 200\
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
  --file './network-contraction-1'

mkdir network-contraction-2
python run-aec-sine.py \
  --dimension 50 100\
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
  --file './network-contraction-2'

mkdir network-contraction-3
python run-aec-sine.py \
  --dimension 200 \
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
  --file './network-contraction-3'

mkdir network-contraction-4
python run-aec-sine.py \
  --dimension 100\
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
  --file './network-contraction-4'




