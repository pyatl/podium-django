PROJECT="podium"

log_message() {
    LOG_MESSAGE=${1?Must specify log message}
    echo "[lint.sh] ${LOG_MESSAGE}"
}

lint() {
    if [ -f lint/results.txt  ]; then
        rm lint/results.txt
    fi
    flake8 --output-file=lint/results.txt --config=lint/flake8
    STATUS=${?}

    # Store a flag saying we ran the linter
    if [ "${STATUS}" == "0" ]; then
        log_message "${PROJECT} has passed the linter."
    else
        log_message "${PROJECT} failed to pass the linter, failing build"
        log_message "Begin Lint Errors"
        cat lint/results.txt
        log_message "End Lint Errors"
    fi

    exit ${STATUS}
}

main() {
    lint
}

main
