params=( 0.0001 0.001 0.01 0.1 1.0 10.0 )

for i in {0..5}
do

mkdir "grid-contraction${i}"
python run-aec-grid.py \
  --dimension 50 100 200 200 100 50\
  --alpha 0. \
  --beta ${params[$i]}  \
  --gamma 0. \
  --sigma 0. \
  --noise 0.1 \
  --npoints 200 \
  --weights 0.14 \
  --stochastic 0 \
  --factor 1 \
  --frate 0 \
  --lrate 0.00001 \
  --inner 200 \
  --outer 100 \
  --file "./grid-contraction${i}"



mkdir "grid-dcontraction${i}"
python run-aec-grid.py \
  --dimension 50 100 200 200 100 50\
  --alpha 0. \
  --beta ${params[$i]} \
  --gamma 1. \
  --sigma 0. \
  --noise 0.1 \
  --npoints 200 \
  --weights 0.14 \
  --stochastic 0 \
  --factor 1 \
  --frate 0 \
  --lrate 0.00001 \
  --inner 200 \
  --outer 100 \
  --file "./grid-dcontraction${i}"



mkdir "grid-ortho${i}"
python run-aec-grid.py \
  --dimension 50 100 200 200 100 50\
  --alpha ${params[$i]}  \
  --beta 0. \
  --gamma 0. \
  --sigma 0. \
  --noise 0.1 \
  --npoints 200 \
  --weights 0.14 \
  --stochastic 0 \
  --factor 1 \
  --frate 0 \
  --lrate 0.00001 \
  --inner 200 \
  --outer 100 \
  --file "./grid-ortho${i}"



mkdir "grid-scheduled-ortho${i}"
python run-aec-grid.py \
  --dimension 50 100 200 200 100 50\
  --alpha ${params[$i]}  \
  --beta 0. \
  --gamma 0. \
  --sigma 0. \
  --noise 0.1 \
  --npoints 200 \
  --weights 0.14 \
  --stochastic 0 \
  --factor 0. \
  --frate 0.0001 \
  --lrate 0.00001 \
  --inner 200 \
  --outer 100 \
  --file "./grid-scheduled-ortho${i}"


mkdir "grid-sqrtortho${i}"
python run-aec-grid.py \
  --dimension 50 100 200 200 100 50\
  --alpha ${params[$i]}  \
  --beta 0. \
  --gamma 0. \
  --sigma 0. \
  --noise 0.1 \
  --npoints 200 \
  --weights 0.14 \
  --stochastic 0 \
  --factor 1 \
  --frate 0 \
  --lrate 0.00001 \
  --inner 200 \
  --outer 100 \
  --tortho "sqrt" \
  --file "./grid-sqrtortho${i}"



mkdir "grid-denoise${i}"
python run-aec-grid.py \
  --dimension 50 100 200 200 100 50\
  --alpha 0. \
  --beta 0. \
  --gamma 0. \
  --sigma ${params[$i]} \
  --noise 0.1 \
  --npoints 200 \
  --weights 0.14 \
  --stochastic 0 \
  --factor 1 \
  --frate 0 \
  --lrate 0.00001 \
  --inner 200 \
  --outer 100 \
  --file "./grid-denoise${i}"



done


