from setuptools import setup

package_name = "threshold_monitor"

setup(
    name=package_name,
    version="0.1.0",
    packages=[package_name],
    install_requires=["setuptools"],
    zip_safe=True,
    maintainer="User",
    maintainer_email="user@example.com",
    description="Threshold monitor node for detecting threshold crossings and stale data.",
    license="Apache-2.0",
    tests_require=["pytest"],
    entry_points={
        "console_scripts": [
            "threshold_monitor = threshold_monitor.threshold_monitor:main",
        ],
    },
)
