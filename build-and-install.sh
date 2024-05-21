python make_ppd.py > zj80.ppd
mkdir -p build
cd build
cmake ..
cmake --build .
sudo make install
