mkdir penalty-ortho-bottleneck-1
python run-aec-sine.py \
  --dimension 50 100 200 100 50 1\
  --alpha 0.04 \
  --beta 0. \
  --gamma 0. \
  --sigma 0. \
  --noise 0.1 \
  --tortho  "" \
  --npoints 100 \
  --weights 0.14 \
  --stochastic 0 \
  --factor 1 \
  --frate 0 \
  --lrate 0.00001 \
  --inner 200 \
  --outer 100 \
  --file './penalty-ortho-bottleneck-1'

mkdir penalty-ortho-bottleneck-2
python run-aec-sine.py \
  --dimension 50 100 200 100 50 1\
  --alpha 0.04 \
  --beta 0. \
  --gamma 0. \
  --sigma 0. \
  --noise 0.1 \
  --tortho "" \
  --npoints 100 \
  --weights 0.14 \
  --stochastic 0 \
  --factor 1 \
  --frate 0 \
  --lrate 0.00001 \
  --inner 200 \
  --outer 100 \
  --file './penalty-ortho-bottleneck-2'

mkdir penalty-ortho-bottleneck-3
python run-aec-sine.py \
  --dimension 50 100 200 100 50 1\
  --alpha 0.02 \
  --beta 0. \
  --gamma 0. \
  --sigma 0. \
  --noise 0.1 \
  --tortho  "" \
  --npoints 100 \
  --weights 0.14 \
  --stochastic 0 \
  --factor 1 \
  --frate 0 \
  --lrate 0.00001 \
  --inner 200 \
  --outer 100 \
  --file './penalty-ortho-bottleneck-3'

mkdir penalty-ortho-bottleneck-4
python run-aec-sine.py \
  --dimension 50 100 200 1\
  --alpha 0.005 \
  --beta 0. \
  --gamma 0. \
  --sigma 0. \
  --noise 0.1 \
  --tortho  "" \
  --npoints 100 \
  --weights 0.14 \
  --stochastic 0 \
  --factor 1 \
  --frate 0 \
  --lrate 0.00001 \
  --inner 200 \
  --outer 100 \
  --file './penalty-ortho-bottleneck-4'


mkdir penalty-ortho-bottleneck-5
python run-aec-sine.py \
  --dimension 50 100 200\
  --alpha 1 \
  --beta 0. \
  --gamma 0. \
  --sigma 0. \
  --noise 0.1 \
  --tortho "" \
  --npoints 100 \
  --weights 0.14 \
  --stochastic 0 \
  --factor 1 \
  --frate 0 \
  --lrate 0.00001 \
  --inner 200 \
  --outer 100 \
  --file './penalty-ortho-bottleneck-5'

mkdir penalty-ortho-bottleneck-6
python run-aec-sine.py \
  --dimension 50 100 200 1\
  --alpha 1 \
  --beta 0. \
  --gamma 0. \
  --sigma 0. \
  --noise 0.1 \
  --tortho  "" \
  --npoints 100 \
  --weights 0.14 \
  --stochastic 0 \
  --factor 1 \
  --frate 0 \
  --lrate 0.00001 \
  --inner 200 \
  --outer 100 \
  --file './penalty-ortho-bottleneck-6'


mkdir penalty-ortho-bottleneck-7
python run-aec-sine.py \
  --dimension 50 100 200 400 1\
  --alpha 0. \
  --beta 0. \
  --gamma 0. \
  --sigma 0. \
  --noise 0.1 \
  --tortho  "" \
  --npoints 100 \
  --weights 0.14 \
  --stochastic 0 \
  --factor 1 \
  --frate 0 \
  --lrate 0.00001 \
  --inner 200 \
  --outer 100 \
  --file './penalty-ortho-bottleneck-7'
