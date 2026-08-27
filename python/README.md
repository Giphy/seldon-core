# Python Module for Seldon Core

# Version Changes

0.2.6

  * Breaking change to route method. Takes a keyword `routing` argument.

0.2.6.1 onwards

  * Python package is for Python > 3.4

## Application tracing

Tracing is enabled with `--tracing` or `TRACING=1`. OpenTelemetry is the
default backend. To send native traces to a Datadog Agent, configure:

```sh
TRACING=1
TRACING_PROVIDER=datadog
SERVICE_NAME=my-model
DD_TRACE_AGENT_URL=http://datadog-agent:8126
```

Datadog's standard `DD_ENV`, `DD_VERSION`, and `DD_TAGS` variables are also
supported. `DD_AGENT_HOST` and `DD_TRACE_AGENT_PORT` can be used instead of
`DD_TRACE_AGENT_URL`. Optional Flask request attributes can be attached to
spans as a comma-separated list in `TRACING_EXTRA_TAGS`.

