params=( 0.0001 0.001 0.01 0.1 1.0 10.0 )

for i in {0..5}
do

#mkdir "spiral-contraction${i}"
#python run-aec-spiral.py \
#  --dimension 100  20  100  20  100 20  100  20  100 20 100  20  100  20 \
#  --alpha 0. \
#  --beta ${params[$i]}  \
#  --gamma 0. \
#  --sigma 0. \
#  --noise 0.03 \
#  --npoints 300 \
#  --weights 0.2 \
#  --stochastic 0 \
#  --factor 1 \
#  --frate 0 \
#  --lrate 0.00001 \
#  --inner 200 \
#  --outer 100 \
#  --file "./spiral-contraction${i}"
#
#
#
#mkdir "spiral-dcontraction${i}"
#python run-aec-spiral.py \
#  --dimension 100  20  100  20  100 20  100  20  100 20 100  20  100  20 \
#  --alpha 0. \
#  --beta ${params[$i]} \
#  --gamma 1. \
#  --sigma 0. \
#  --noise 0.03 \
#  --npoints 300 \
#  --weights 0.2 \
#  --stochastic 0 \
#  --factor 1 \
#  --frate 0 \
#  --lrate 0.00001 \
#  --inner 200 \
#  --outer 100 \
#  --file "./spiral-dcontraction${i}"



#mkdir "spiral-ortho${i}"
#python run-aec-spiral.py \
#  --dimension 100  20  100  20  100 20  100  20  100 20 100  20  100  20 \
#  --alpha ${params[$i]}  \
#  --beta 0. \
#  --gamma 0. \
#  --sigma 0. \
#  --noise 0.03 \
#  --npoints 300 \
#  --weights 0.2 \
#  --stochastic 0 \
#  --factor 1 \
#  --frate 0 \
#  --lrate 0.00001 \
#  --inner 200 \
#  --outer 100 \
#  --file "./spiral-ortho${i}"



mkdir "spiral-scheduled-ortho${i}"
python run-aec-spiral.py \
  --dimension 100  20  100  20  100 20  100  20  100 20 100  20  100  20 \
  --alpha ${params[$i]}  \
  --beta 0. \
  --gamma 0. \
  --sigma 0. \
  --noise 0.03 \
  --npoints 300 \
  --weights 0.2 \
  --stochastic 0 \
  --factor 0. \
  --frate 0.0001 \
  --lrate 0.00001 \
  --inner 200 \
  --outer 100 \
  --file "./spiral-scheduled-ortho${i}"


#mkdir "spiral-sqrtortho${i}"
#python run-aec-spiral.py \
#  --dimension 100  20  100  20  100 20  100  20  100 20 100  20  100  20 \
#  --alpha ${params[$i]}  \
#  --beta 0. \
#  --gamma 0. \
#  --sigma 0. \
#  --noise 0.03 \
#  --npoints 300 \
#  --weights 0.2 \
#  --stochastic 0 \
#  --factor 1 \
#  --frate 0 \
#  --lrate 0.00001 \
#  --inner 200 \
#  --outer 100 \
#  --tortho "sqrt" \
#  --file "./spiral-sqrtortho${i}"



#mkdir "spiral-denoise${i}"
#python run-aec-spiral.py \
#  --dimension 100  20  100  20  100 20  100  20  100 20 100  20  100  20 \
#  --alpha 0. \
#  --beta 0. \
#  --gamma 0. \
#  --sigma ${params[$i]} \
#  --noise 0.03 \
#  --npoints 300 \
#  --weights 0.2 \
#  --stochastic 0 \
#  --factor 1 \
#  --frate 0 \
#  --lrate 0.00001 \
#  --inner 200 \
#  --outer 100 \
#  --file "./spiral-denoise${i}"



done
