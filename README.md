

Project 1: AI Security Foundations and Threat Modelling

Overview
Establishes the security foundation for an AI-powered application by identifying potential threats, analysing risks and documenting appropriate security controls.

Objectives

- Understand AI application architecture and security boundaries.
- Identify threats affecting users, AI agents, APIs and data.
- Apply the STRIDE threat modelling methodology.
- Assess security risks and recommend mitigations.

Methodology – STRIDE

Threat| Description
Spoofing| Impersonating a legitimate user or AI agent
Tampering| Modifying requests, responses or data
Repudiation| Denying actions without sufficient audit evidence
Information Disclosure| Exposing confidential information
Denial of Service| Disrupting service availability
Elevation of Privilege| Gaining unauthorised permissions

Security Areas

- Authentication and authorisation
- API security
- AI prompt security
- Data confidentiality
- Agent identity and permissions
- Logging and monitoring

Deliverables

- AI system security analysis
- STRIDE threat mapping
- Risk assessment
- Security mitigation recommendations
- Supporting screenshots and documentation

---

Project 2: AI Identity and Access Management (IAM) Design

Overview
Focuses on designing secure identity and access management for AI applications and agents through authentication, token management and controlled resource access.

Objectives

- Understand authentication and authorisation.
- Explore OAuth 2.0 and OpenID Connect (OIDC).
- Demonstrate secure authentication flows.
- Understand machine-to-machine authentication.
- Apply the principle of least privilege.

Technologies and Tools

- Auth0
- OAuth 2.0
- OpenID Connect (OIDC)
- JWT
- PKCE
- Python
- Visual Studio Code
- GitHub
- 
Key Implementation Areas
Auth0 Configuration
Configure an application and identity provider settings for authentication.
PKCE Authentication Flow
Explore Proof Key for Code Exchange to protect authorisation-code-based authentication.
Machine-to-Machine Authentication
Demonstrate how services and AI agents can authenticate without interactive user login.
Token Security
Examine JWT claims, token expiration, issuer, audience and scopes.
Access Control
Document role-based permissions and least-privilege access for AI agents.

Deliverables

- IAM design and authentication flow
- Auth0 configuration evidence
- Token inspection evidence
- Access-control recommendations
- Supporting screenshots and documentation

---

Project 3: Red Team – AI Identity Attacks

Overview
Explores potential attacks against AI applications, agent identities and connected resources using controlled security simulations.

Objectives

- Understand AI-specific security threats.
- Demonstrate prompt injection and identity spoofing.
- Explore system prompt extraction.
- Simulate RAG poisoning and MCP abuse.
- Assess vulnerability severity using CVSS 3.1.
- Map relevant attacks to OWASP and MITRE ATLAS.

Technologies and Tools

- Python
- JWT
- CVSS 3.1
- OWASP Top 10 for LLM Applications
- MITRE ATLAS
- Visual Studio Code
- GitHub

Attack Scenarios

1. Indirect Prompt Injection
Simulate malicious instructions that attempt to influence AI application behaviour.
2. Agent Identity Spoofing
Demonstrate how a spoofed agent identity or sender label can influence a mock privileged action.
3. System Prompt Extraction
Explore techniques that attempt to reveal hidden system instructions.
4. RAG Poisoning and MCP Abuse
Simulate malicious knowledge-base content and unauthorised mock tool execution.
5. CVSS Vulnerability Assessment
Assess selected findings using CVSS 3.1 and document severity.
6. MITRE ATLAS Mapping
Map relevant AI attack techniques to the MITRE ATLAS knowledge base.

Deliverables

- Red-team attack demonstrations
- Attack reports and screenshots
- CVSS vulnerability assessment
- MITRE ATLAS mapping
- Attack success analysis

---

Project 4: Blue Team – AI Security Defence

Overview

Focuses on defensive security measures for AI applications, including input and output guardrails, cryptographic agent identity, token security and anomaly detection.

Objectives

- Develop defensive controls against AI-specific attacks.
- Detect suspicious prompts and sensitive output patterns.
- Demonstrate cryptographic message verification.
- Explore identity-provider security settings.
- Identify suspicious authentication and agent activity.
- Compare attack behaviour before and after defensive controls.

Technologies and Tools

- Python
- Auth0
- Flask
- Ed25519 cryptography
- JWT
- Regular expressions
- NeMo Guardrails configuration exploration
- Visual Studio Code
- GitHub

Key Defensive Controls

1. Input and Output Guardrails
Use pattern-based checks to identify suspicious input and detect or redact JWT-shaped strings in output.

2. Cryptographic Agent Identity
Use Ed25519 public-key cryptography to demonstrate message signing, signature verification and tamper detection.

3. Auth0 Security Hardening
Explore access-token lifetime configuration, refresh-token rotation and authentication security settings.

4. Anomaly Detection
Demonstrate detection rules for:
- Unusual request spikes
- Unexpected scope changes
- Expired-token reuse

5. Security Effectiveness Analysis
Compare selected attack scenarios with defensive controls and document observed results.
Deliverables
- Guardrail implementation
- Ed25519 signature verification demonstration
- Auth0 configuration evidence
- Anomaly detection alerts
- Before-and-after security analysis
- Supporting screenshots and reports
