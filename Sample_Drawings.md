# Professional Mermaid Diagrams Showcase

A collection of high-quality, aesthetically pleasing Mermaid diagrams for system architecture, workflows, and technical documentation.

---

## 1. System Architecture Diagrams

### Example 1.1: Microservices Architecture
```mermaid
graph TB
    subgraph "Client Layer"
        Web[Web Client]
        Mobile[Mobile App]
        Desktop[Desktop App]
    end
    
    subgraph "API Gateway Layer"
        Gateway[API Gateway<br/>Load Balancer]
    end
    
    subgraph "Service Layer"
        Auth[Authentication<br/>Service]
        User[User<br/>Service]
        Order[Order<br/>Service]
        Payment[Payment<br/>Service]
        Notification[Notification<br/>Service]
    end
    
    subgraph "Data Layer"
        UserDB[(User DB<br/>PostgreSQL)]
        OrderDB[(Order DB<br/>MongoDB)]
        Cache[(Redis<br/>Cache)]
        Queue[Message Queue<br/>RabbitMQ]
    end
    
    subgraph "External Services"
        Email[Email Provider]
        SMS[SMS Gateway]
        Analytics[Analytics Platform]
    end
    
    Web --> Gateway
    Mobile --> Gateway
    Desktop --> Gateway
    
    Gateway --> Auth
    Gateway --> User
    Gateway --> Order
    Gateway --> Payment
    
    Auth --> UserDB
    User --> UserDB
    User --> Cache
    
    Order --> OrderDB
    Order --> Queue
    Payment --> Queue
    
    Queue --> Notification
    Notification --> Email
    Notification --> SMS
    
    Order --> Analytics
    Payment --> Analytics
    
    style Web fill:#4A90E2,stroke:#2E5C8A,stroke-width:2px,color:#fff
    style Mobile fill:#4A90E2,stroke:#2E5C8A,stroke-width:2px,color:#fff
    style Desktop fill:#4A90E2,stroke:#2E5C8A,stroke-width:2px,color:#fff
    style Gateway fill:#F5A623,stroke:#C67D00,stroke-width:3px,color:#fff
    style Auth fill:#7ED321,stroke:#5FA019,stroke-width:2px,color:#fff
    style User fill:#7ED321,stroke:#5FA019,stroke-width:2px,color:#fff
    style Order fill:#7ED321,stroke:#5FA019,stroke-width:2px,color:#fff
    style Payment fill:#7ED321,stroke:#5FA019,stroke-width:2px,color:#fff
    style Notification fill:#7ED321,stroke:#5FA019,stroke-width:2px,color:#fff
    style UserDB fill:#BD10E0,stroke:#8B0AA8,stroke-width:2px,color:#fff
    style OrderDB fill:#BD10E0,stroke:#8B0AA8,stroke-width:2px,color:#fff
    style Cache fill:#FF6B6B,stroke:#CC5555,stroke-width:2px,color:#fff
    style Queue fill:#FF6B6B,stroke:#CC5555,stroke-width:2px,color:#fff
```

### Example 1.2: Cloud Infrastructure Architecture
```mermaid
graph TB
    subgraph "Users"
        U1[End Users]
    end
    
    subgraph "CDN & DNS"
        CDN[CloudFlare CDN]
        DNS[Route 53 DNS]
    end
    
    subgraph "AWS Cloud - us-east-1"
        subgraph "VPC"
            subgraph "Public Subnet"
                ALB[Application<br/>Load Balancer]
                NAT[NAT Gateway]
            end
            
            subgraph "Private Subnet - AZ1"
                EC2_1[EC2 Instance<br/>Web Server 1]
                EC2_2[EC2 Instance<br/>App Server 1]
            end
            
            subgraph "Private Subnet - AZ2"
                EC2_3[EC2 Instance<br/>Web Server 2]
                EC2_4[EC2 Instance<br/>App Server 2]
            end
            
            subgraph "Data Tier"
                RDS[(RDS Multi-AZ<br/>PostgreSQL)]
                ElastiCache[(ElastiCache<br/>Redis Cluster)]
                S3[(S3 Bucket<br/>Static Assets)]
            end
        end
    end
    
    subgraph "Monitoring & Security"
        CloudWatch[CloudWatch<br/>Monitoring]
        GuardDuty[GuardDuty<br/>Threat Detection]
        WAF[AWS WAF]
    end
    
    U1 --> CDN
    CDN --> DNS
    DNS --> WAF
    WAF --> ALB
    
    ALB --> EC2_1
    ALB --> EC2_3
    
    EC2_1 --> EC2_2
    EC2_3 --> EC2_4
    
    EC2_2 --> RDS
    EC2_4 --> RDS
    
    EC2_2 --> ElastiCache
    EC2_4 --> ElastiCache
    
    EC2_1 --> S3
    EC2_3 --> S3
    
    EC2_2 --> NAT
    EC2_4 --> NAT
    
    ALB -.-> CloudWatch
    EC2_1 -.-> CloudWatch
    EC2_2 -.-> CloudWatch
    EC2_3 -.-> CloudWatch
    EC2_4 -.-> CloudWatch
    RDS -.-> CloudWatch
    
    WAF -.-> GuardDuty
    
    style U1 fill:#FFE5CC,stroke:#FF9933,stroke-width:2px
    style CDN fill:#00D4FF,stroke:#0099CC,stroke-width:2px,color:#000
    style DNS fill:#00D4FF,stroke:#0099CC,stroke-width:2px,color:#000
    style WAF fill:#FF6B6B,stroke:#CC0000,stroke-width:2px,color:#fff
    style ALB fill:#FF9900,stroke:#CC7700,stroke-width:3px,color:#fff
    style NAT fill:#FF9900,stroke:#CC7700,stroke-width:2px,color:#fff
    style EC2_1 fill:#FF9900,stroke:#CC7700,stroke-width:2px,color:#fff
    style EC2_2 fill:#FF9900,stroke:#CC7700,stroke-width:2px,color:#fff
    style EC2_3 fill:#FF9900,stroke:#CC7700,stroke-width:2px,color:#fff
    style EC2_4 fill:#FF9900,stroke:#CC7700,stroke-width:2px,color:#fff
    style RDS fill:#3B48CC,stroke:#2A3699,stroke-width:2px,color:#fff
    style ElastiCache fill:#CC3B3B,stroke:#992A2A,stroke-width:2px,color:#fff
    style S3 fill:#569A31,stroke:#3D6E22,stroke-width:2px,color:#fff
    style CloudWatch fill:#FF4F8B,stroke:#CC3366,stroke-width:2px,color:#fff
    style GuardDuty fill:#FF4F8B,stroke:#CC3366,stroke-width:2px,color:#fff
```

### Example 1.3: Event-Driven Architecture
```mermaid
graph LR
    subgraph "Event Sources"
        API[REST API]
        UI[Web UI]
        Mobile[Mobile App]
        IoT[IoT Devices]
    end
    
    subgraph "Event Bus"
        EventBridge[AWS EventBridge<br/>Event Router]
    end
    
    subgraph "Event Processors"
        Lambda1[Lambda<br/>Order Processor]
        Lambda2[Lambda<br/>Payment Processor]
        Lambda3[Lambda<br/>Notification Service]
        Lambda4[Lambda<br/>Analytics Engine]
    end
    
    subgraph "Event Store"
        EventStore[(Event Store<br/>DynamoDB Streams)]
        Analytics[(Analytics DB<br/>Redshift)]
    end
    
    subgraph "Downstream Systems"
        Email[Email Service<br/>SES]
        SMS[SMS Service<br/>SNS]
        Webhook[External Webhooks]
        Dashboard[Real-time Dashboard]
    end
    
    API --> EventBridge
    UI --> EventBridge
    Mobile --> EventBridge
    IoT --> EventBridge
    
    EventBridge --> Lambda1
    EventBridge --> Lambda2
    EventBridge --> Lambda3
    EventBridge --> Lambda4
    
    Lambda1 --> EventStore
    Lambda2 --> EventStore
    Lambda3 --> EventStore
    Lambda4 --> Analytics
    
    Lambda3 --> Email
    Lambda3 --> SMS
    Lambda1 --> Webhook
    Lambda4 --> Dashboard
    
    style API fill:#4ECDC4,stroke:#3AA99F,stroke-width:2px,color:#fff
    style UI fill:#4ECDC4,stroke:#3AA99F,stroke-width:2px,color:#fff
    style Mobile fill:#4ECDC4,stroke:#3AA99F,stroke-width:2px,color:#fff
    style IoT fill:#4ECDC4,stroke:#3AA99F,stroke-width:2px,color:#fff
    style EventBridge fill:#FF6B6B,stroke:#CC5555,stroke-width:4px,color:#fff
    style Lambda1 fill:#FFD93D,stroke:#CCB030,stroke-width:2px,color:#000
    style Lambda2 fill:#FFD93D,stroke:#CCB030,stroke-width:2px,color:#000
    style Lambda3 fill:#FFD93D,stroke:#CCB030,stroke-width:2px,color:#000
    style Lambda4 fill:#FFD93D,stroke:#CCB030,stroke-width:2px,color:#000
    style EventStore fill:#6BCB77,stroke:#52A05E,stroke-width:2px,color:#fff
    style Analytics fill:#6BCB77,stroke:#52A05E,stroke-width:2px,color:#fff
```

---

## 2. Sequence Diagrams

### Example 2.1: OAuth 2.0 Authentication Flow
```mermaid
sequenceDiagram
    participant User
    participant Client as Client App
    participant Auth as Auth Server
    participant Resource as Resource Server
    participant DB as Database
    
    autonumber
    
    User->>Client: 1. Request Access
    activate Client
    Client->>Auth: 2. Authorization Request<br/>(client_id, redirect_uri)
    activate Auth
    
    Auth->>User: 3. Login Page
    User->>Auth: 4. Credentials
    Auth->>DB: 5. Validate User
    activate DB
    DB-->>Auth: 6. User Valid
    deactivate DB
    
    Auth->>User: 7. Consent Screen
    User->>Auth: 8. Grant Permission
    
    Auth->>Client: 9. Authorization Code
    deactivate Auth
    
    Client->>Auth: 10. Token Request<br/>(code, client_secret)
    activate Auth
    Auth->>DB: 11. Verify Code
    activate DB
    DB-->>Auth: 12. Code Valid
    deactivate DB
    
    Auth->>Client: 13. Access Token + Refresh Token
    deactivate Auth
    deactivate Client
    
    Note over Client,Auth: Token Obtained Successfully
    
    Client->>Resource: 14. API Request<br/>(Access Token)
    activate Resource
    Resource->>Auth: 15. Validate Token
    activate Auth
    Auth-->>Resource: 16. Token Valid
    deactivate Auth
    
    Resource->>DB: 17. Fetch Data
    activate DB
    DB-->>Resource: 18. User Data
    deactivate DB
    
    Resource->>Client: 19. Protected Resource
    deactivate Resource
    Client->>User: 20. Display Data
    
    rect rgb(200, 240, 200)
        Note over User,DB: Successful Authentication Flow
    end
```

### Example 2.2: Distributed Transaction - Saga Pattern
```mermaid
sequenceDiagram
    participant Client
    participant OrderSvc as Order Service
    participant PaymentSvc as Payment Service
    participant InventorySvc as Inventory Service
    participant ShippingSvc as Shipping Service
    participant EventBus as Event Bus
    
    autonumber
    
    Client->>OrderSvc: Create Order
    activate OrderSvc
    
    OrderSvc->>EventBus: OrderCreated Event
    activate EventBus
    EventBus->>PaymentSvc: Process Payment
    activate PaymentSvc
    
    alt Payment Successful
        PaymentSvc->>EventBus: PaymentCompleted Event
        EventBus->>InventorySvc: Reserve Inventory
        activate InventorySvc
        
        alt Inventory Available
            InventorySvc->>EventBus: InventoryReserved Event
            EventBus->>ShippingSvc: Create Shipment
            activate ShippingSvc
            ShippingSvc->>EventBus: ShipmentCreated Event
            deactivate ShippingSvc
            
            EventBus->>OrderSvc: All Steps Complete
            OrderSvc->>Client: Order Confirmed ✓
            
            rect rgb(200, 250, 200)
                Note over Client,EventBus: Success Path - Happy Flow
            end
            
        else Inventory Unavailable
            InventorySvc->>EventBus: InventoryFailed Event
            deactivate InventorySvc
            
            EventBus->>PaymentSvc: Compensate: Refund Payment
            PaymentSvc->>EventBus: PaymentRefunded Event
            deactivate PaymentSvc
            
            EventBus->>OrderSvc: Order Failed - Inventory
            OrderSvc->>Client: Order Failed ✗<br/>(Insufficient Inventory)
            
            rect rgb(255, 200, 200)
                Note over Client,EventBus: Compensation - Inventory Failure
            end
        end
        
    else Payment Failed
        PaymentSvc->>EventBus: PaymentFailed Event
        deactivate PaymentSvc
        EventBus->>OrderSvc: Order Failed - Payment
        OrderSvc->>Client: Order Failed ✗<br/>(Payment Declined)
        
        rect rgb(255, 200, 200)
            Note over Client,EventBus: Early Failure - Payment Declined
        end
    end
    
    deactivate EventBus
    deactivate OrderSvc
```

---

## 3. Flowcharts

### Example 3.1: CI/CD Pipeline Flow
```mermaid
flowchart TD
    Start([Developer Pushes Code]) --> Webhook{Webhook<br/>Triggered?}
    
    Webhook -->|Yes| Clone[Clone Repository]
    Webhook -->|No| End1([Process Failed])
    
    Clone --> Install[Install Dependencies<br/>npm install]
    Install --> Lint[Run Linter<br/>ESLint]
    
    Lint --> LintCheck{Lint<br/>Passed?}
    LintCheck -->|No| Notify1[Notify Developer<br/>Lint Errors]
    Notify1 --> End2([Build Failed])
    
    LintCheck -->|Yes| Test[Run Unit Tests<br/>Jest/Mocha]
    Test --> TestCheck{All Tests<br/>Passed?}
    
    TestCheck -->|No| Notify2[Notify Developer<br/>Test Failures]
    Notify2 --> End3([Build Failed])
    
    TestCheck -->|Yes| Build[Build Application<br/>Webpack/Rollup]
    Build --> BuildCheck{Build<br/>Successful?}
    
    BuildCheck -->|No| Notify3[Notify Developer<br/>Build Errors]
    Notify3 --> End4([Build Failed])
    
    BuildCheck -->|Yes| Security[Security Scan<br/>Snyk/SonarQube]
    Security --> SecurityCheck{Vulnerabilities<br/>Found?}
    
    SecurityCheck -->|Critical| Notify4[Block Deployment<br/>Critical Issues]
    Notify4 --> End5([Deployment Blocked])
    
    SecurityCheck -->|Minor/None| Docker[Build Docker Image<br/>docker build]
    Docker --> Push[Push to Registry<br/>ECR/Docker Hub]
    
    Push --> Branch{Branch?}
    
    Branch -->|develop| DeployDev[Deploy to Dev<br/>ECS/K8s]
    DeployDev --> SmokeTest1[Run Smoke Tests]
    SmokeTest1 --> Success1([Deployed to Dev ✓])
    
    Branch -->|staging| DeployStage[Deploy to Staging<br/>ECS/K8s]
    DeployStage --> IntegrationTest[Integration Tests<br/>Selenium/Cypress]
    IntegrationTest --> TestStage{Tests<br/>Passed?}
    TestStage -->|Yes| Success2([Deployed to Staging ✓])
    TestStage -->|No| Rollback1[Rollback Staging]
    Rollback1 --> End6([Deployment Failed])
    
    Branch -->|main| Approval{Manual<br/>Approval?}
    Approval -->|Denied| End7([Deployment Cancelled])
    Approval -->|Approved| DeployProd[Deploy to Production<br/>Blue/Green]
    
    DeployProd --> HealthCheck[Health Checks<br/>Load Balancer]
    HealthCheck --> HealthOK{Healthy?}
    
    HealthOK -->|No| Rollback2[Automatic Rollback<br/>Previous Version]
    Rollback2 --> Alert[Alert On-Call Team]
    Alert --> End8([Deployment Failed])
    
    HealthOK -->|Yes| Switch[Switch Traffic<br/>100% to New Version]
    Switch --> Monitor[Monitor Metrics<br/>15 minutes]
    Monitor --> MetricsOK{Metrics<br/>Normal?}
    
    MetricsOK -->|No| Rollback3[Emergency Rollback]
    Rollback3 --> End9([Deployment Failed])
    
    MetricsOK -->|Yes| Cleanup[Cleanup Old Resources]
    Cleanup --> Success3([Deployed to Prod ✓])
    
    style Start fill:#4ECDC4,stroke:#3AA99F,stroke-width:2px,color:#fff
    style Clone fill:#95E1D3,stroke:#71B8A8,stroke-width:2px
    style Install fill:#95E1D3,stroke:#71B8A8,stroke-width:2px
    style Lint fill:#95E1D3,stroke:#71B8A8,stroke-width:2px
    style Test fill:#95E1D3,stroke:#71B8A8,stroke-width:2px
    style Build fill:#95E1D3,stroke:#71B8A8,stroke-width:2px
    style Security fill:#FFD93D,stroke:#CCB030,stroke-width:2px
    style Docker fill:#38B6FF,stroke:#2D8FCC,stroke-width:2px,color:#fff
    style Push fill:#38B6FF,stroke:#2D8FCC,stroke-width:2px,color:#fff
    style DeployDev fill:#A8E6CF,stroke:#7FB89D,stroke-width:2px
    style DeployStage fill:#FFD93D,stroke:#CCB030,stroke-width:2px
    style DeployProd fill:#FF6B9D,stroke:#CC5580,stroke-width:2px,color:#fff
    style Success1 fill:#6BCB77,stroke:#52A05E,stroke-width:2px,color:#fff
    style Success2 fill:#6BCB77,stroke:#52A05E,stroke-width:2px,color:#fff
    style Success3 fill:#6BCB77,stroke:#52A05E,stroke-width:2px,color:#fff
    style End1 fill:#FF6B6B,stroke:#CC5555,stroke-width:2px,color:#fff
    style End2 fill:#FF6B6B,stroke:#CC5555,stroke-width:2px,color:#fff
    style End3 fill:#FF6B6B,stroke:#CC5555,stroke-width:2px,color:#fff
    style End4 fill:#FF6B6B,stroke:#CC5555,stroke-width:2px,color:#fff
    style End5 fill:#FF6B6B,stroke:#CC5555,stroke-width:2px,color:#fff
    style End6 fill:#FF6B6B,stroke:#CC5555,stroke-width:2px,color:#fff
    style End7 fill:#FF6B6B,stroke:#CC5555,stroke-width:2px,color:#fff
    style End8 fill:#FF6B6B,stroke:#CC5555,stroke-width:2px,color:#fff
    style End9 fill:#FF6B6B,stroke:#CC5555,stroke-width:2px,color:#fff
```

### Example 3.2: Machine Learning Pipeline
```mermaid
flowchart TB
    Start([Start ML Pipeline]) --> DataSource{Data Source<br/>Type?}
    
    DataSource -->|Database| ExtractDB[(Extract from<br/>PostgreSQL)]
    DataSource -->|API| ExtractAPI[Fetch from<br/>REST API]
    DataSource -->|Files| ExtractFiles[Read from<br/>S3/GCS]
    
    ExtractDB --> Clean
    ExtractAPI --> Clean
    ExtractFiles --> Clean
    
    Clean[Data Cleaning<br/>Remove nulls, duplicates] --> Validate{Data Quality<br/>Check}
    
    Validate -->|Failed| Alert1[Alert Data Team<br/>Quality Issues]
    Alert1 --> End1([Pipeline Failed])
    
    Validate -->|Passed| Transform[Feature Engineering<br/>Scaling, Encoding]
    Transform --> Split[Train/Test Split<br/>80/20]
    
    Split --> Parallel1{Processing<br/>Mode?}
    
    Parallel1 -->|Single Model| TrainSingle[Train Model<br/>XGBoost/RandomForest]
    Parallel1 -->|Ensemble| TrainMulti[Train Multiple Models<br/>Parallel Processing]
    
    TrainSingle --> Evaluate
    TrainMulti --> Evaluate
    
    Evaluate[Model Evaluation<br/>Cross-Validation] --> MetricsCheck{Metrics<br/>Acceptable?}
    
    MetricsCheck -->|No| Tune[Hyperparameter Tuning<br/>GridSearch/Bayesian]
    Tune --> Retrain[Retrain with<br/>Optimal Params]
    Retrain --> Evaluate
    
    MetricsCheck -->|Yes| Compare{Better than<br/>Baseline?}
    
    Compare -->|No| Alert2[Keep Existing Model<br/>Notify Team]
    Alert2 --> End2([No Deployment])
    
    Compare -->|Yes| Package[Package Model<br/>Docker Container]
    Package --> Test[A/B Testing<br/>Shadow Mode]
    
    Test --> TestResults{A/B Test<br/>Results?}
    
    TestResults -->|Worse| Rollback[Keep Old Version]
    Rollback --> End3([Deployment Cancelled])
    
    TestResults -->|Better| Deploy{Deployment<br/>Strategy?}
    
    Deploy -->|Canary| Canary[Deploy to 5% Traffic]
    Deploy -->|Blue-Green| BlueGreen[Deploy to New Cluster]
    
    Canary --> Monitor1[Monitor Performance<br/>1 hour]
    BlueGreen --> Monitor1
    
    Monitor1 --> Stable{Performance<br/>Stable?}
    
    Stable -->|No| Emergency[Emergency Rollback<br/>Revert to Old Model]
    Emergency --> End4([Deployment Failed])
    
    Stable -->|Yes| FullDeploy[Deploy to 100%<br/>Production Traffic]
    FullDeploy --> Log[Log Model Version<br/>MLflow/Weights & Biases]
    
    Log --> Schedule[Schedule Retraining<br/>Next Week]
    Schedule --> Success([Pipeline Complete ✓])
    
    style Start fill:#667EEA,stroke:#4C63B6,stroke-width:2px,color:#fff
    style Clean fill:#48BB78,stroke:#38A169,stroke-width:2px,color:#fff
    style Transform fill:#48BB78,stroke:#38A169,stroke-width:2px,color:#fff
    style Split fill:#48BB78,stroke:#38A169,stroke-width:2px,color:#fff
    style TrainSingle fill:#F6AD55,stroke:#DD6B20,stroke-width:2px,color:#fff
    style TrainMulti fill:#F6AD55,stroke:#DD6B20,stroke-width:2px,color:#fff
    style Evaluate fill:#F6AD55,stroke:#DD6B20,stroke-width:2px,color:#fff
    style Tune fill:#ED8936,stroke:#C05621,stroke-width:2px,color:#fff
    style Package fill:#4299E1,stroke:#2B6CB0,stroke-width:2px,color:#fff
    style Test fill:#4299E1,stroke:#2B6CB0,stroke-width:2px,color:#fff
    style Canary fill:#9F7AEA,stroke:#6B46C1,stroke-width:2px,color:#fff
    style BlueGreen fill:#9F7AEA,stroke:#6B46C1,stroke-width:2px,color:#fff
    style FullDeploy fill:#9F7AEA,stroke:#6B46C1,stroke-width:2px,color:#fff
    style Success fill:#48BB78,stroke:#2F855A,stroke-width:3px,color:#fff
    style End1 fill:#F56565,stroke:#C53030,stroke-width:2px,color:#fff
    style End2 fill:#F56565,stroke:#C53030,stroke-width:2px,color:#fff
    style End3 fill:#F56565,stroke:#C53030,stroke-width:2px,color:#fff
    style End4 fill:#F56565,stroke:#C53030,stroke-width:2px,color:#fff
```

---

## 4. State Diagrams

### Example 4.1: Order State Machine
```mermaid
stateDiagram-v2
    [*] --> Draft: Create Order
    
    Draft --> PendingPayment: Submit Order
    Draft --> Cancelled: Cancel by User
    
    PendingPayment --> Processing: Payment Confirmed
    PendingPayment --> PaymentFailed: Payment Declined
    PendingPayment --> Cancelled: Timeout (30 min)
    
    PaymentFailed --> PendingPayment: Retry Payment
    PaymentFailed --> Cancelled: Max Retries Exceeded
    
    Processing --> InventoryCheck: Validate Stock
    
    InventoryCheck --> Confirmed: Stock Available
    InventoryCheck --> OutOfStock: Stock Unavailable
    
    OutOfStock --> Refunding: Auto Refund
    OutOfStock --> Backordered: Allow Backorder
    
    Backordered --> Confirmed: Stock Replenished
    
    Confirmed --> Preparing: Allocate Inventory
    
    Preparing --> ReadyToShip: Packed & Labeled
    Preparing --> Cancelled: Cancel by User
    
    ReadyToShip --> Shipped: Carrier Pickup
    
    Shipped --> InTransit: In Delivery Network
    
    InTransit --> OutForDelivery: At Local Hub
    InTransit --> DeliveryAttempted: Failed Delivery
    
    DeliveryAttempted --> OutForDelivery: Reschedule
    DeliveryAttempted --> ReturnToSender: Max Attempts
    
    OutForDelivery --> Delivered: Successful Delivery
    OutForDelivery --> DeliveryAttempted: Failed Delivery
    
    Delivered --> Completed: Confirmed by Customer
    Delivered --> ReturnRequested: Return Initiated
    
    ReturnRequested --> ReturnInProgress: Return Approved
    ReturnRequested --> Completed: Return Denied
    
    ReturnInProgress --> Refunding: Return Received
    
    Refunding --> Refunded: Refund Processed
    
    ReturnToSender --> Refunding: Received at Warehouse
    
    Refunded --> [*]
    Cancelled --> [*]
    Completed --> [*]
    
    note right of Draft
        Initial state
        Order can be modified
    end note
    
    note right of PendingPayment
        Awaiting payment
        30 min timeout
    end note
    
    note right of Confirmed
        Payment successful
        Stock reserved
        No cancellation allowed
    end note
    
    note right of Delivered
        Customer has 14 days
        to request return
    end note
```

### Example 4.2: User Session State
```mermaid
stateDiagram-v2
    [*] --> Anonymous: User Visits Site
    
    Anonymous --> Registering: Click Sign Up
    Anonymous --> LoggingIn: Click Login
    Anonymous --> BrowsingGuest: Browse as Guest
    
    Registering --> EmailVerification: Submit Registration
    EmailVerification --> Active: Verify Email
    EmailVerification --> Anonymous: Verification Failed
    
    LoggingIn --> Active: Valid Credentials
    LoggingIn --> Locked: Failed 5 Attempts
    LoggingIn --> Anonymous: Cancel
    
    Locked --> LoggingIn: Wait 15 Minutes
    Locked --> PasswordReset: Forgot Password
    
    PasswordReset --> LoggingIn: Reset Complete
    
    BrowsingGuest --> LoggingIn: Decide to Login
    BrowsingGuest --> Registering: Decide to Register
    BrowsingGuest --> [*]: Leave Site
    
    Active --> Browsing: Browse Content
    Active --> Shopping: View Products
    Active --> AccountSettings: Manage Account
    
    Browsing --> Active: Return to Dashboard
    Shopping --> Active: Return to Dashboard
    AccountSettings --> Active: Save Changes
    
    Active --> Inactive: No Activity (15 min)
    Inactive --> Active: User Action
    Inactive --> [*]: Session Timeout (30 min)
    
    Active --> [*]: Logout
    Browsing --> [*]: Logout
    Shopping --> [*]: Logout
    AccountSettings --> [*]: Logout
    
    state Active {
        [*] --> Dashboard
        Dashboard --> Profile: View Profile
        Dashboard --> Messages: Check Messages
        Dashboard --> Notifications: View Notifications
        
        Profile --> Dashboard: Back
        Messages --> Dashboard: Back
        Notifications --> Dashboard: Back
    }
    
    state Shopping {
        [*] --> ProductList
        ProductList --> ProductDetail: Select Product
        ProductDetail --> Cart: Add to Cart
        Cart --> Checkout: Proceed
        Checkout --> PaymentProcessing: Submit Order
        PaymentProcessing --> OrderComplete: Payment Success
        PaymentProcessing --> Cart: Payment Failed
        OrderComplete --> [*]
    }
```

---

## 5. Entity Relationship Diagrams

### Example 5.1: E-commerce Database Schema
```mermaid
erDiagram
    CUSTOMER ||--o{ ORDER : places
    CUSTOMER ||--o{ REVIEW : writes
    CUSTOMER ||--o{ WISHLIST : maintains
    CUSTOMER {
        int customer_id PK
        string email UK
        string password_hash
        string first_name
        string last_name
        string phone
        date date_of_birth
        datetime created_at
        datetime updated_at
        boolean is_active
        string customer_tier
    }
    
    ORDER ||--|{ ORDER_ITEM : contains
    ORDER ||--|| PAYMENT : has
    ORDER ||--|| SHIPPING : has
    ORDER {
        int order_id PK
        int customer_id FK
        decimal total_amount
        string status
        datetime order_date
        datetime estimated_delivery
        string shipping_address
        string billing_address
    }
    
    ORDER_ITEM }o--|| PRODUCT : references
    ORDER_ITEM {
        int order_item_id PK
        int order_id FK
        int product_id FK
        int quantity
        decimal unit_price
        decimal discount
        decimal subtotal
    }
    
    PRODUCT ||--o{ REVIEW : receives
    PRODUCT ||--o{ PRODUCT_IMAGE : has
    PRODUCT ||--|| CATEGORY : belongs_to
    PRODUCT ||--o{ INVENTORY : tracked_in
    PRODUCT {
        int product_id PK
        int category_id FK
        string name
        text description
        decimal price
        decimal cost
        string sku UK
        int stock_quantity
        boolean is_active
        datetime created_at
        float average_rating
    }
    
    CATEGORY ||--o{ CATEGORY : parent_of
    CATEGORY {
        int category_id PK
        int parent_category_id FK
        string name
        text description
        string slug UK
        int display_order
        boolean is_active
    }
    
    PAYMENT {
        int payment_id PK
        int order_id FK
        decimal amount
        string payment_method
        string transaction_id
        string status
        datetime payment_date
        string gateway_response
    }
    
    SHIPPING {
        int shipping_id PK
        int order_id FK
        string carrier
        string tracking_number
        string status
        datetime shipped_date
        datetime delivered_date
        decimal shipping_cost
    }
    
    REVIEW {
        int review_id PK
        int product_id FK
        int customer_id FK
        int rating
        text comment
        datetime review_date
        int helpful_count
        boolean is_verified_purchase
    }
    
    WISHLIST {
        int wishlist_id PK
        int customer_id FK
        int product_id FK
        datetime added_date
        int priority
    }
    
    INVENTORY {
        int inventory_id PK
        int product_id FK
        int warehouse_id FK
        int quantity
        string location
        datetime last_updated
    }
    
    PRODUCT_IMAGE {
        int image_id PK
        int product_id FK
        string image_url
        int display_order
        boolean is_primary
    }
```

---

## 6. Class Diagrams

### Example 6.1: Payment Processing System
```mermaid
classDiagram
    class PaymentProcessor {
        <<interface>>
        +processPayment(amount, currency) PaymentResult
        +refundPayment(transactionId) RefundResult
        +validatePayment(paymentInfo) boolean
    }
    
    class CreditCardProcessor {
        -string merchantId
        -string apiKey
        -int retryAttempts
        +processPayment(amount, currency) PaymentResult
        +refundPayment(transactionId) RefundResult
        +validatePayment(paymentInfo) boolean
        -encryptCardData(cardInfo) string
        -sendToGateway(payload) Response
    }
    
    class PayPalProcessor {
        -string clientId
        -string clientSecret
        -string environment
        +processPayment(amount, currency) PaymentResult
        +refundPayment(transactionId) RefundResult
        +validatePayment(paymentInfo) boolean
        -getAccessToken() string
        -createOrder(amount) OrderId
    }
    
    class StripeProcessor {
        -string publishableKey
        -string secretKey
        +processPayment(amount, currency) PaymentResult
        +refundPayment(transactionId) RefundResult
        +validatePayment(paymentInfo) boolean
        -createPaymentIntent(amount) PaymentIntent
        -confirmPayment(intentId) boolean
    }
    
    class PaymentResult {
        +string transactionId
        +string status
        +decimal amount
        +datetime timestamp
        +string errorMessage
        +boolean isSuccessful()
        +string getReceiptUrl()
    }
    
    class RefundResult {
        +string refundId
        +string originalTransactionId
        +decimal refundAmount
        +string status
        +datetime processedAt
    }
    
    class Payment {
        -int paymentId
        -decimal amount
        -string currency
        -string method
        -string status
        -datetime createdAt
        +void authorize()
        +void capture()
        +void void()
        +void refund(amount)
    }
    
    class Transaction {
        -string transactionId
        -int paymentId
        -string type
        -decimal amount
        -string status
        -datetime timestamp
        +void record()
        +void rollback()
    }
    
    class PaymentGateway {
        -PaymentProcessor processor
        -Logger logger
        -MetricsCollector metrics
        +PaymentResult process(Payment payment)
        +RefundResult refund(string transactionId, decimal amount)
        -void logTransaction(Transaction tx)
        -void emitMetric(string eventName)
    }
    
    class FraudDetection {
        -MLModel fraudModel
        -RiskThreshold threshold
        +FraudScore analyze(Payment payment)
        +boolean shouldBlock(FraudScore score)
        -void updateModel(Transaction tx)
    }
    
    class FraudScore {
        +float score
        +string riskLevel
        +List~string~ flags
        +string recommendation
    }
    
    PaymentProcessor <|.. CreditCardProcessor : implements
    PaymentProcessor <|.. PayPalProcessor : implements
    PaymentProcessor <|.. StripeProcessor : implements
    
    PaymentGateway --> PaymentProcessor : uses
    PaymentGateway --> FraudDetection : uses
    PaymentGateway --> Transaction : creates
    
    Payment --> Transaction : has
    Payment --> PaymentResult : produces
    
    FraudDetection --> FraudScore : generates
    FraudDetection --> Payment : analyzes
    
    PaymentProcessor --> PaymentResult : returns
    PaymentProcessor --> RefundResult : returns
```

---

## 7. Gantt Charts

### Example 7.1: Software Development Project Timeline
```mermaid
gantt
    title Software Development Project - Q1 2024
    dateFormat YYYY-MM-DD
    section Planning Phase
    Requirements Gathering           :done,    req1, 2024-01-01, 2024-01-10
    System Design                     :done,    des1, 2024-01-08, 2024-01-20
    Architecture Review               :done,    arch1, 2024-01-18, 2024-01-22
    Sprint Planning                   :done,    sprint1, 2024-01-22, 2024-01-24
    
    section Backend Development
    Database Schema Design            :done,    db1, 2024-01-25, 2024-02-05
    API Development - Auth            :done,    api1, 2024-02-05, 2024-02-15
    API Development - Core Features   :active,  api2, 2024-02-15, 2024-03-05
    Integration Testing               :         test1, 2024-03-01, 2024-03-10
    Performance Optimization          :         perf1, 2024-03-05, 2024-03-15
    
    section Frontend Development
    UI/UX Design                      :done,    ui1, 2024-01-25, 2024-02-10
    Component Library Setup           :done,    comp1, 2024-02-10, 2024-02-15
    Dashboard Development             :active,  dash1, 2024-02-15, 2024-03-05
    User Management Pages             :         user1, 2024-03-01, 2024-03-12
    Responsive Design Implementation  :         resp1, 2024-03-08, 2024-03-18
    
    section DevOps & Infrastructure
    CI/CD Pipeline Setup              :done,    cicd1, 2024-02-01, 2024-02-08
    Containerization                  :done,    dock1, 2024-02-08, 2024-02-12
    Cloud Infrastructure Setup        :active,  cloud1, 2024-02-12, 2024-02-25
    Monitoring & Logging              :         mon1, 2024-02-20, 2024-03-05
    Security Hardening                :         sec1, 2024-03-01, 2024-03-15
    
    section Testing & QA
    Unit Testing                      :         unit1, 2024-02-20, 2024-03-15
    Integration Testing               :         int1, 2024-03-05, 2024-03-20
    User Acceptance Testing           :         uat1, 2024-03-15, 2024-03-25
    Bug Fixing                        :crit,    bug1, 2024-03-20, 2024-03-28
    
    section Deployment
    Staging Deployment                :         stage1, 2024-03-22, 2024-03-24
    Production Deployment             :crit,    prod1, 2024-03-28, 2024-03-29
    Post-Launch Monitoring            :         monitor1, 2024-03-29, 2024-04-05
```

---

## 8. Git Graph

### Example 8.1: Feature Branch Workflow
```mermaid
gitgraph
    commit id: "Initial commit"
    commit id: "Setup project structure"
    
    branch develop
    checkout develop
    commit id: "Add base configuration"
    commit id: "Setup database schema"
    
    branch feature/user-auth
    checkout feature/user-auth
    commit id: "Add user model"
    commit id: "Implement JWT auth"
    commit id: "Add login endpoint"
    
    checkout develop
    branch feature/product-catalog
    checkout feature/product-catalog
    commit id: "Add product model"
    commit id: "Implement CRUD endpoints"
    
    checkout develop
    merge feature/user-auth tag: "v0.1.0"
    
    checkout feature/product-catalog
    commit id: "Add product images"
    commit id: "Implement search"
    
    checkout develop
    merge feature/product-catalog tag: "v0.2.0"
    
    branch feature/shopping-cart
    checkout feature/shopping-cart
    commit id: "Add cart model"
    commit id: "Implement cart operations"
    
    checkout develop
    commit id: "Update dependencies"
    commit id: "Fix security vulnerability"
    
    checkout feature/shopping-cart
    merge develop
    commit id: "Add cart persistence"
    commit id: "Implement checkout flow"
    
    checkout develop
    merge feature/shopping-cart tag: "v0.3.0"
    
    branch release/1.0
    checkout release/1.0
    commit id: "Update version to 1.0.0"
    commit id: "Final testing & bug fixes"
    
    checkout main
    merge release/1.0 tag: "v1.0.0"
    
    checkout develop
    merge release/1.0
    
    branch hotfix/critical-bug
    checkout hotfix/critical-bug
    commit id: "Fix critical payment bug"
    
    checkout main
    merge hotfix/critical-bug tag: "v1.0.1"
    
    checkout develop
    merge hotfix/critical-bug
```

---

## 9. User Journey Maps

### Example 9.1: E-commerce User Journey
```mermaid
journey
    title E-commerce Purchase Journey
    section Discovery
      Browse homepage: 5: Customer
      Search for product: 4: Customer
      View search results: 4: Customer, SearchEngine
      Click on product: 5: Customer
    section Evaluation
      View product details: 5: Customer
      Read reviews: 4: Customer
      Compare similar products: 3: Customer
      Add to wishlist: 4: Customer
      Check shipping info: 4: Customer, ShippingService
    section Decision
      Add to cart: 5: Customer
      View cart: 5: Customer
      Apply coupon code: 5: Customer, PromotionEngine
      Proceed to checkout: 5: Customer
    section Checkout
      Enter shipping address: 3: Customer
      Select shipping method: 4: Customer, ShippingService
      Enter payment details: 3: Customer
      Review order: 4: Customer
      Place order: 5: Customer, PaymentProcessor
    section Post-Purchase
      Receive confirmation email: 5: Customer, EmailService
      Track shipment: 4: Customer, LogisticsService
      Receive product: 5: Customer, DeliveryService
      Write review: 4: Customer
      Share on social media: 3: Customer, SocialMedia
```

---

## 10. Timeline Diagrams

### Example 10.1: System Evolution Timeline
```mermaid
timeline
    title System Architecture Evolution (2020-2024)
    
    section 2020 - Monolith Era
        Q1 : Single Server Deployment
           : MySQL Database
           : Manual Deployments
        Q2 : Added Load Balancer
           : Vertical Scaling
        Q3 : Database Replication
           : Read Replicas
        Q4 : CDN Integration
           : Basic Monitoring
    
    section 2021 - Cloud Migration
        Q1 : Migrated to AWS
           : EC2 Auto Scaling
        Q2 : S3 for Static Assets
           : CloudFront CDN
        Q3 : RDS Multi-AZ
           : ElastiCache Redis
        Q4 : ECS Containerization
           : Docker Images
    
    section 2022 - Microservices
        Q1 : Service Decomposition
           : API Gateway
        Q2 : Event-Driven Architecture
           : Message Queues
        Q3 : Service Mesh (Istio)
           : Circuit Breakers
        Q4 : Kubernetes Migration
           : Helm Charts
    
    section 2023 - Observability
        Q1 : Distributed Tracing
           : Jaeger Implementation
        Q2 : Prometheus Metrics
           : Grafana Dashboards
        Q3 : Log Aggregation
           : ELK Stack
        Q4 : Chaos Engineering
           : Resilience Testing
    
    section 2024 - AI/ML Integration
        Q1 : ML Feature Store
           : Model Serving Platform
        Q2 : Real-time Recommendations
           : Personalization Engine
        Q3 : Predictive Analytics
           : Anomaly Detection
        Q4 : Edge Computing (Planned)
           : 5G Integration (Planned)
```

---

## Usage Tips

### 1. **Styling Guidelines**
- Use consistent color schemes across similar diagram types
- Lighter colors for less critical components
- Darker/bold colors for critical paths or components
- Red tones for errors, failures, or critical alerts
- Green tones for success states
- Blue tones for processing states
- Yellow/orange for warnings or intermediate states

### 2. **Best Practices**
- Keep diagrams focused on a single aspect or flow
- Use subgraphs to group related components
- Add clear labels and descriptions
- Include legends when using many colors
- Use notes to add context
- Keep hierarchy clear with proper indentation

### 3. **Accessibility**
- Don't rely solely on color to convey meaning
- Use text labels in addition to colors
- Ensure sufficient contrast
- Use different shapes for different types of nodes

### 4. **Performance**
- Very large diagrams (100+ nodes) may render slowly
- Consider breaking complex diagrams into multiple smaller ones
- Use links between diagrams to maintain relationships

---

## Customization Examples

### Color Palette Suggestions

**Professional Corporate:**
- Primary: #2C3E50 (Dark Blue)
- Secondary: #3498DB (Light Blue)
- Success: #27AE60 (Green)
- Warning: #F39C12 (Orange)
- Error: #E74C3C (Red)

**Modern Tech:**
- Primary: #667EEA (Purple)
- Secondary: #4FD1C5 (Teal)
- Success: #48BB78 (Green)
- Warning: #F6AD55 (Orange)
- Error: #F56565 (Red)

**Minimalist:**
- Primary: #1A202C (Almost Black)
- Secondary: #718096 (Gray)
- Success: #38B2AC (Teal)
- Warning: #ED8936 (Orange)
- Error: #FC8181 (Pink)

---

**This is a living document. Feel free to adapt and extend these examples for your specific use cases!**
