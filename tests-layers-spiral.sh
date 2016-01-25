

mkdir "layers-spiral-contraction1"
python run-aec-spiral.py \
  --dimension 100 \
  --alpha 0. \
  --beta 0.1  \
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
  --file "./layers-spiral-contraction1"

mkdir "layers-spiral-contraction2"
python run-aec-spiral.py \
  --dimension 100 100\
  --alpha 0. \
  --beta 0.1  \
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
  --file "./layers-spiral-contraction2"


mkdir "layers-spiral-contraction3"
python run-aec-spiral.py \
  --dimension 100 100 100\
  --alpha 0. \
  --beta 0.1  \
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
  --file "./layers-spiral-contraction3"


mkdir "layers-spiral-contraction3"
python run-aec-spiral.py \
  --dimension 100 100 100 100\
  --alpha 0. \
  --beta 0.1  \
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
  --file "./layers-spiral-contraction3"


mkdir "layers-spiral-contraction4"
python run-aec-spiral.py \
  --dimension 100 100 100 100 100\
  --alpha 0. \
  --beta 0.1  \
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
  --file "./layers-spiral-contraction4"




done
