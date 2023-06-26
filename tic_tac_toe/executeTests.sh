# !/bin/bash
# Executes the tests for the project.

# abort on nonzero exitstatus
set -o errexit
# abort on unbound variable
set -o nounset
# don't hide errors within pipes
set -o pipefail

script_name=$(basename "${0}")
script_dir=$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )
readonly script_name script_dir

echo "Executing tests in ${script_dir}..."

pushd ./tests
python -m unittest discover
popd

echo "Tests executed."