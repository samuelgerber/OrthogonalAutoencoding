mkdir penalty-ortho-1
python run-aec-sine.py \
  --dimension 50 100 200\
  --alpha 0.04 \
  --beta 0. \
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
  --file './penalty-ortho-1'




mkdir penalty-ortho-2
python run-aec-sine.py \
  --dimension 50 100 200\
  --alpha 0.02 \
  --beta 0. \
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
  --file './penalty-ortho-2'



mkdir penalty-ortho-3
python run-aec-sine.py \
  --dimension 50 100 200\
  --alpha 0.01 \
  --beta 0. \
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
  --file './penalty-ortho-3'

mkdir penalty-ortho-4
python run-aec-sine.py \
  --dimension 50 100 200\
  --alpha 0.005 \
  --beta 0. \
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
  --file './penalty-ortho-4'

mkdir penalty-ortho-5
python run-aec-sine.py \
  --dimension 50 100 200\
  --alpha 0.001 \
  --beta 0. \
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
  --file './penalty-ortho-5'

