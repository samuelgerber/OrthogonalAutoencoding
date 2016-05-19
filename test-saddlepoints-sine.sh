mkdir sp-sine-contraction
python run-aec-sine.py \
  --dimension 50 100 200 200 100 50\
  --alpha 0. \
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
  --file './sp-sine-contraction'

mkdir sp-sine-contraction-ortho
python run-aec-sine.py \
  --dimension 50 50\
  --alpha 0.1 \
  --tortho ""\
  --beta 0.005 \
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
  --file './sp-sine-contraction-ortho'

mkdir sp-sine-contraction-ortho-squared
python run-aec-sine.py \
  --dimension 50 100 200 200 100 50\
  --alpha 0.1 \
  --tortho "squared"\
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
  --file './sp-sine-contraction-ortho-squared'


mkdir sp-sine-denoise
python run-aec-sine.py \
  --dimension 50 100 200 200 100 50\
  --alpha 0. \
  --beta 0 \
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
  --file './sp-sine-denoise'

mkdir sp-sine-denoise-ortho-tmp
python run-aec-sine.py \
  --dimension 50 50\
  --alpha 1. \
  --tortho ""\
  --beta 0. \
  --gamma 0. \
  --sigma 0.1 \
  --noise 0.1 \
  --npoints 100 \
  --weights 0.14 \
  --stochastic 0 \
  --factor 1 \
  --frate 0 \
  --lrate 0.00001 \
  --inner 200 \
  --outer 100 \
  --file './sp-sine-denoise-ortho-tmp'


mkdir sp-sine-denoise-ortho2
python run-aec-sine.py \
  --dimension 50 100 200 200 100 50\
  --alpha 10 \
  --tortho ""\
  --beta 0. \
  --gamma 0. \
  --sigma 0.1 \
  --noise 0.1 \
  --npoints 100 \
  --weights 0.14 \
  --stochastic 0 \
  --factor 1 \
  --frate 0 \
  --lrate 0.00001 \
  --inner 200 \
  --outer 100 \
  --file './sp-sine-denoise-ortho2'



mkdir sp-sine-denoise-ortho-squared
python run-aec-sine.py \
  --dimension 50 100 200 200 100 50\
  --alpha 0.1 \
  --tortho "squared"\
  --beta 0. \
  --gamma 0. \
  --sigma 0.1 \
  --noise 0.1 \
  --npoints 100 \
  --weights 0.14 \
  --stochastic 0 \
  --factor 1 \
  --frate 0 \
  --lrate 0.00001 \
  --inner 200 \
  --outer 100 \
  --file './sp-sine-denoise-ortho-squared'



mkdir sp-sine-ortho
python run-aec-sine.py \
  --dimension 50 100 200 200 100 50\
  --alpha 1. \
  --tortho ""\
  --beta 0. \
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
  --file './sp-sine-ortho'



mkdir sp-sine-ortho-squared
python run-aec-sine.py \
  --dimension 50 100 200 200 100 50\
  --alpha 0.1 \
  --tortho "squared"\
  --beta 0. \
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
  --file './sp-sine-ortho-squared'


