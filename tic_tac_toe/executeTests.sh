#!/bin/bash
# Executes the tests for the project.

# abort on nonzero exitstatus
set -o errexit
# abort on unbound variable
set -o nounset
# don't hide errors within pipes
set -o pipefail

script_dir=$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)
test_dir="${script_dir}/tests"
readonly script_dir

echo "Executing tests in ${test_dir}..."
(
    cd "${test_dir}"
    python -m unittest discover
)

echo "Tests executed."
