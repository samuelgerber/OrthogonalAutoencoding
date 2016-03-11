mkdir penalty-bottleneck-1
python run-aec-sine.py \
  --dimension 50 100 200 1\
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
  --lrate 0.0002 \
  --inner 200 \
  --outer 100 \
  --file './penalty-bottleneck-1'

mkdir penalty-bottleneck-2
python run-aec-sine.py \
  --dimension 50 100 200 1\
  --alpha 0. \
  --beta 0.02 \
  --gamma 0. \
  --sigma 0. \
  --noise 0.1 \
  --tortho "" \
  --npoints 100 \
  --weights 0.14 \
  --stochastic 0 \
  --factor 1 \
  --frate 0 \
  --lrate 0.0002 \
  --inner 200 \
  --outer 100 \
  --file './penalty-bottleneck-2'

mkdir penalty-bottleneck-3
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
  --lrate 0.0002 \
  --inner 200 \
  --outer 100 \
  --file './penalty-bottleneck-3'

