# Base grafana image
FROM grafana/grafana:8.2.6

# Swap original config file for the custom one
ADD ./grafana.ini /etc/grafana/grafana.ini

# Add provisioning
ADD ./provisioning /etc/grafana/provisioning

# Add dashboard json files
ADD ./dashboards /etc/grafana/dashboards

# Run service
CMD ["service", "grafana-server", "restart"]