mkdir penalty-denoise-1
python run-aec-sine.py \
  --dimension 50 100 200\
  --alpha 0. \
  --beta 0. \
  --gamma 0. \
  --sigma 0.2 \
  --noise 0.1 \
  --npoints 100 \
  --weights 0.14 \
  --stochastic 0 \
  --factor 1 \
  --frate 0 \
  --lrate 0.0001 \
  --inner 200 \
  --outer 100 \
  --file './penalty-denoise-1'




mkdir penalty-denoise-2
python run-aec-sine.py \
  --dimension 50 100 200\
  --alpha 1 \
  --tortho "" \
  --beta 0. \
  --gamma 0. \
  --sigma 0.2 \
  --noise 0.1 \
  --npoints 100 \
  --weights 0.14 \
  --stochastic 0 \
  --factor 1 \
  --frate 0 \
  --lrate 0.0001 \
  --inner 200 \
  --outer 100 \
  --file './penalty-denoise-2'


mkdir penalty-denoise-3
python run-aec-sine.py \
  --dimension 50 100 200\
  --alpha 0. \
  --tortho "" \
  --beta 0.01 \
  --gamma 0. \
  --sigma 0.2 \
  --noise 0.1 \
  --npoints 100 \
  --weights 0.14 \
  --stochastic 0 \
  --factor 1 \
  --frate 0 \
  --lrate 0.0001 \
  --inner 200 \
  --outer 100 \
  --file './penalty-denoise-3'

mkdir penalty-denoise-4
python run-aec-sine.py \
  --dimension 50 100 200\
  --alpha 0. \
  --tortho "" \
  --beta 0.02 \
  --gamma 0. \
  --sigma 0.2 \
  --noise 0.1 \
  --npoints 100 \
  --weights 0.14 \
  --stochastic 0 \
  --factor 1 \
  --frate 0 \
  --lrate 0.0001 \
  --inner 200 \
  --outer 100 \
  --file './penalty-denoise-4'


