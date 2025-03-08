from plantuml import PlantUML

def generate_uml_diagram(uml_code, output_file):
    server = PlantUML(url="http://www.plantuml.com/plantuml/png/")
    with open(output_file, "wb") as f:
        f.write(server.processes(uml_code))

uml_kubernetes = """
@startuml

skinparam dpi 300

package "Kubernetes Cluster" {
    package "Monitoring" {
        [Prometheus (Monitoring)] --> [Grafana (Visualization)]: Queries Metrics
    }
    
    package "Orchestration" {
        [Horizontal Pod Autoscaler (HPA)] --> [CRUD Service]: Scales Based on CPU Usage
    }
    
    package "Chaos Engineering" {
        [Chaos Mesh (Fault Tolerance)] --> [Prometheus (Monitoring)]: Simulates Failures
        [Chaos Mesh (Fault Tolerance)] --> [Kafka Consumer]: Simulates Failures
        [Chaos Mesh (Fault Tolerance)] --> [CRUD Service]: Simulates Failures
    }
}

note right of [Chaos Mesh (Fault Tolerance)]
Chaos Mesh simulates:
- Pod Crashes
- Network Partitions
- Resource Contention
end note

note right of [HPA]
HPA dynamically scales:
- CRUD Service based on CPU usage
- Can use custom metrics (e.g., Kafka lag)
end note

@enduml
"""

uml_event_streaming = """
@startuml

skinparam dpi 300

package "Event Streaming Platform" {
    [Kafka] --> [Kafka Consumer]: Subscribes to Topics
    [Kafka] --> [MongoDB]: Stores Events
    [Kafka] --> [CRUD Service]: Publishes Events
    [Kafka] --> [gRPC Service]: Publishes Events
    
    package "Cluster Coordination" {
        [Zookeeper] --> [Kafka]: Coordinates Cluster
    }
}

[External REST Clients] --> [CRUD Service]: HTTP Requests
[gRPC Clients] --> [gRPC Service]: gRPC Communication

note right of [Kafka]
Kafka Fault Tolerance:
- Topic Replication
- Zookeeper Coordination
- Leader Election
end note

note right of [MongoDB]
MongoDB Replica Set ensures:
- Data Replication
- High Availability
- Automatic Failover
end note

' Connection point to Figure 1
[CRUD Service] ..> [Prometheus (Monitoring)] : Connects to Figure 1
[gRPC Service] ..> [Prometheus (Monitoring)] : Connects to Figure 1

@enduml
"""

# Generate UML diagrams
generate_uml_diagram(uml_kubernetes, "kubernetes_diagram.png")
generate_uml_diagram(uml_event_streaming, "event_streaming_diagram.png")
