echo "Executing tests..."

pushd ./tests
python -m unittest discover
popd

echo "Tests executed."