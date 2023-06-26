echo "Executing tests..."

ls
pushd ./tests
python -m unittest discover
popd

echo "Tests executed."