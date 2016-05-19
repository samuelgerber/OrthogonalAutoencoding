
mkdir penalty-d-contraction-ortho
python run-aec-sine.py \
  --dimension 50 100 200\
  --alpha 1 \
  --tortho ""\
  --beta 0.01 \
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
  --file './penalty-d-contraction-ortho'

mkdir penalty-d-denoise-ortho
python run-aec-sine.py \
  --dimension 50 100 200\
  --alpha 10 \
  --tortho ""\
  --beta 0. \
  --gamma 0. \
  --sigma 0.2 \
  --noise 0.1 \
  --npoints 100 \
  --weights 0.14 \
  --stochastic 0 \
  --factor 1 \
  --frate 0 \
  --lrate 0.00001 \
  --inner 200 \
  --outer 100 \
  --file './penalty-d-denoise-ortho'

