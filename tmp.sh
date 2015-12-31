

mkdir spiral-sqrtortho5
python run-aec-spiral.py \
  --dimension 100  20  100  20  100 20  100  20  100 20 100  20  100  20 \
  --alpha 1 \
  --tortho 'sqrt' \
  --beta 0. \
  --gamma 0. \
  --sigma 0. \
  --noise 0.03 \
  --npoints 300 \
  --weights 0.2 \
  --stochastic 0 \
  --factor 1 \
  --frate 0 \
  --lrate 0.00001 \
  --inner 200 \
  --outer 100 \
  --file './spiral-sqrtortho5'

mkdir spiral-sqrtortho6
python run-aec-spiral.py \
  --dimension 100  20  100  20  100 20  100  20  100 20 100  20  100  20 \
  --alpha 10 \
  --tortho 'sqrt' \
  --beta 0. \
  --gamma 0. \
  --sigma 0. \
  --noise 0.03 \
  --npoints 300 \
  --weights 0.2 \
  --stochastic 0 \
  --factor 1 \
  --frate 0 \
  --lrate 0.00001 \
  --inner 200 \
  --outer 100 \
  --file './spiral-sqrtortho6'

