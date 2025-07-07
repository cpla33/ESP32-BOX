sudo apt update; sudo apt upgrade -y
python3 -m pip install --upgrade pip
pip3 install esphome
esphome run test_outputs.yaml
