mkdir spiral-bottleneck-1
python run-aec-spiral.py \
  --dimension 10 200 200 400 200 200 10 1\
  --alpha 0. \
  --beta 0. \
  --gamma 0. \
  --sigma 0. \
  --noise 0.05 \
  --npoints 200 \
  --weights 0.14 \
  --stochastic 0 \
  --factor 1 \
  --frate 0 \
  --lrate 0.00001 \
  --inner 200 \
  --outer 100 \
  --file './spiral-bottleneck-1'


mkdir spiral-bottleneck-2
python run-aec-spiral.py \
  --dimension 50 100 200 100 50 1\
  --alpha 0. \
  --beta 0. \
  --gamma 0. \
  --sigma 0. \
  --noise 0.05 \
  --npoints 200 \
  --weights 0.14 \
  --stochastic 0 \
  --factor 1 \
  --frate 0 \
  --lrate 0.00001 \
  --inner 200 \
  --outer 100 \
  --file './spiral-bottleneck-2'



mkdir spiral-bottleneck-3
python run-aec-spiral.py \
  --dimension 50 100 50  1\
  --alpha 0. \
  --beta 0. \
  --gamma 0. \
  --sigma 0. \
  --noise 0.05 \
  --npoints 200 \
  --weights 0.14 \
  --stochastic 0 \
  --factor 1 \
  --frate 0 \
  --lrate 0.00001 \
  --inner 200 \
  --outer 100 \
  --file './spiral-bottleneck-3'


mkdir spiral-bottleneck-4
python run-aec-spiral.py \
  --dimension 100 1\
  --alpha 0. \
  --beta 0. \
  --gamma 0. \
  --sigma 0. \
  --noise 0.05 \
  --npoints 200 \
  --weights 0.14 \
  --stochastic 0 \
  --factor 1 \
  --frate 0 \
  --lrate 0.00001 \
  --inner 200 \
  --outer 100 \
  --file './spiral-bottleneck-4'

