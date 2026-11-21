set -euo pipefail

if [ "$#" -ne 3 ]; then
    echo "Usage: $0 <WHITE|BLACK> <timeout-seconds> <server-ip>" >&2
    exit 1
fi

ROLE="$(echo "$1" | tr '[:lower:]' '[:upper:]')" 
TIMEOUT="$2"
SERVER_IP="$3"

if [ "$ROLE" != "WHITE" ] && [ "$ROLE" != "BLACK" ]; then
    echo "Error: role must be WHITE or BLACK (got '$1')" >&2
    exit 1
fi

if ! [[ "$TIMEOUT" =~ ^[0-9]+$ ]] || [ "$TIMEOUT" -le 0 ]; then
    echo "Error: timeout must be a positive integer (got '$TIMEOUT')" >&2
    exit 1
fi


SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"


exec uv run --no-sync python -m tablut "$ROLE" "$TIMEOUT" "$SERVER_IP"