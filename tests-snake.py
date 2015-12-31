params=( 0.0001 0.001 0.01 0.1 1.0 10.0 )

for i in {0..5}
do

mkdir "snake-contraction${i}"
python run-aec-sine.py \
  --dimension 50 100 200 200 100 50\
  --alpha 0. \
  --beta ${params[$i]}  \
  --gamma 0. \
  --sigma 0. \
  --noise 0.5 \
  --width 0.5 \
  --npoints 200 \
  --weights 0.14 \
  --stochastic 0 \
  --factor 1 \
  --frate 0 \
  --lrate 0.00001 \
  --inner 200 \
  --outer 100 \
  --file "./snake-contraction${i}"



mkdir "snake-dcontraction${i}"
python run-aec-sine.py \
  --dimension 50 100 200 200 100 50\
  --alpha 0. \
  --beta ${params[$i]} \
  --gamma 1. \
  --sigma 0. \
  --noise 0.5 \
  --width 0.5 \
  --npoints 200 \
  --weights 0.14 \
  --stochastic 0 \
  --factor 1 \
  --frate 0 \
  --lrate 0.00001 \
  --inner 200 \
  --outer 100 \
  --file "./snake-dcontraction${i}"



mkdir "snake-ortho${i}"
python run-aec-sine.py \
  --dimension 50 100 200 200 100 50\
  --alpha ${params[$i]}  \
  --beta 0. \
  --gamma 0. \
  --sigma 0. \
  --noise 0.5 \
  --width 0.5 \
  --npoints 200 \
  --weights 0.14 \
  --stochastic 0 \
  --factor 1 \
  --frate 0 \
  --lrate 0.00001 \
  --inner 200 \
  --outer 100 \
  --file "./snake-ortho${i}"



mkdir "snake-scheduled-ortho${i}"
python run-aec-sine.py \
  --dimension 50 100 200 200 100 50\
  --alpha ${params[$i]}  \
  --beta 0. \
  --gamma 0. \
  --sigma 0. \
  --noise 0.5 \
  --width 0.5 \
  --npoints 200 \
  --weights 0.14 \
  --stochastic 0 \
  --factor 0. \
  --frate 0.0001 \
  --lrate 0.00001 \
  --inner 200 \
  --outer 100 \
  --file "./snake-scheduled-ortho${i}"


mkdir "snake-sqrtortho${i}"
python run-aec-sine.py \
  --dimension 50 100 200 200 100 50\
  --alpha ${params[$i]}  \
  --beta 0. \
  --gamma 0. \
  --sigma 0. \
  --noise 0.5 \
  --width 0.5 \
  --npoints 200 \
  --weights 0.14 \
  --stochastic 0 \
  --factor 1 \
  --frate 0 \
  --lrate 0.00001 \
  --inner 200 \
  --outer 100 \
  --tortho "sqrt" \
  --file "./snake-sqrtortho${i}"



mkdir "snake-denoise${i}"
python run-aec-sine.py \
  --dimension 50 100 200 200 100 50\
  --alpha 0. \
  --beta 0. \
  --gamma 0. \
  --sigma ${params[$i]} \
  --noise 0.5 \
  --width 0.5 \
  --npoints 200 \
  --weights 0.14 \
  --stochastic 0 \
  --factor 1 \
  --frate 0 \
  --lrate 0.00001 \
  --inner 200 \
  --outer 100 \
  --file "./snake-denoise${i}"



done



