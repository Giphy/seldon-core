import os
from itertools import chain

from setuptools import find_packages, setup

# Extra dependencies, with special 'all' key
extras = {"tensorflow": ["tensorflow>=2.21.0,<3.0.0"]}
all_extra_deps = chain.from_iterable(extras.values())
extras["all"] = list(set(all_extra_deps))

setup(
    name="seldon-core",
    author="Seldon Technologies Ltd.",
    author_email="hello@seldon.io",
    version="1.17.1",
    description="Seldon Core client and microservice wrapper",
    url="https://github.com/SeldonIO/seldon-core",
    license="Apache 2.0",
    license_files=["LICENSE"],
    packages=find_packages(),
    include_package_data=True,
    python_requires=">=3.12",
    install_requires=[
        "Flask>=3.1.3,<4.0.0",
        "jsonschema>=4.26.0,<5.0.0",
        "Flask-Cors>=6.0.5,<7.0.0",
        "requests>=2.34.2,<3.0.0",
        "numpy>=2.5.2,<3.0.0",
        "protobuf>=7.36.0,<8.0.0",
        "grpcio>=1.83.0,<2.0.0",
        "grpcio-reflection>=1.83.0,<2.0.0",
        "gunicorn>=26.2.0,<27.0.0",
        "prometheus-client>=0.26.0,<1.0.0",
        "werkzeug>=3.1.8,<4.0.0",
        "cryptography>=50.0.1,<51.0.0",
        "PyYAML>=6.0.3,<7.0.0",
        "click>=8.5.0,<9.0.0",
        "urllib3>=2.7.0,<3.0.0",
        "opentelemetry-api>=1.44.0,<2.0.0",
        "opentelemetry-sdk>=1.44.0,<2.0.0",
        "opentelemetry-exporter-otlp-proto-grpc>=1.44.0,<2.0.0",
        "opentelemetry-instrumentation-flask>=0.65b0,<1.0.0",
        "opentelemetry-instrumentation-grpc>=0.65b0,<1.0.0",
        "ddtrace>=4.14.0,<5.0.0",
    ],
    extras_require=extras,
    entry_points={
        "console_scripts": [
            "seldon-core-microservice = seldon_core.microservice:main",
            "seldon-core-tester = seldon_core.microservice_tester:main",
            "seldon-core-microservice-tester = seldon_core.microservice_tester:main",
            "seldon-core-api-tester = seldon_core.api_tester:main",
            "seldon-batch-processor = seldon_core.batch_processor:run_cli",
        ]
    },
    zip_safe=False,
)
