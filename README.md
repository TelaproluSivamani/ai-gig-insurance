# AI Gig Insurance Platform

## Problem Statement

Gig economy delivery workers such as **Swiggy, Zomato, Amazon, and Zepto riders** often lose income due to **external disruptions** like heavy rain, extreme heat, pollution, or local restrictions.

These disruptions reduce working hours and can decrease a worker’s weekly earnings by **20–30%**. Currently, gig workers do not have insurance that protects their **income loss caused by environmental disruptions**.

---

## Proposed Solution

AI Gig Insurance is an **AI-powered parametric insurance platform** that automatically compensates gig workers when disruptions occur.

Instead of manual claims, the system uses **real-time environmental triggers** such as weather conditions and pollution levels to automatically detect disruptions and process payouts.

---

## Target Persona

**Persona:** Food Delivery Riders

Example Worker:

* Name: Ravi
* Platform: Swiggy
* Location: Hyderabad
* Daily Income: ₹800

### Scenario

If heavy rain occurs in Ravi's delivery zone and deliveries stop for several hours, the system automatically triggers a claim and compensates his income loss.

---

## End-to-End Workflow

1. Worker registers on the platform
2. AI model calculates **risk score**
3. System determines **weekly premium**
4. Weather and environmental APIs monitor conditions
5. Parametric triggers detect disruptions
6. Claim automatically initiated
7. Payment is processed to the worker

---

## Parametric Triggers

| Trigger          | Condition                 |
| ---------------- | ------------------------- |
| Heavy Rain       | Rainfall > 70mm           |
| Heatwave         | Temperature > 42°C        |
| Severe Pollution | AQI > 400                 |
| Flood Alert      | Government weather alerts |

---

## AI Components

### Risk Prediction Model

AI calculates risk score based on:

* Temperature
* Rainfall
* Pollution index (AQI)

### Premium Prediction Model

Weekly premium determined based on predicted risk.

Example:

| Risk Level  | Weekly Premium |
| ----------- | -------------- |
| Low Risk    | ₹20            |
| Medium Risk | ₹40            |
| High Risk   | ₹60            |

### Fraud Detection

Detects:

* Duplicate claims
* Invalid locations
* GPS spoofing attempts

---

## Technology Stack

Frontend
React.js

Backend
FastAPI (Python)

Database
SQLite

Machine Learning
Python + Scikit-learn

APIs
Weather API (mock)
Pollution API (mock)

Payment Integration
Simulated UPI payout system

---

## System Architecture

User Interface (React)
↓
Backend API (FastAPI)
↓
AI Models (Risk + Premium + Fraud Detection)
↓
Trigger Engine (Weather / Pollution)
↓
Claim Processing System
↓
Payment API

---

## Development Roadmap

### Phase 1

Architecture design, prototype, AI model simulation.

### Phase 2

Insurance policy management and automated claims.

### Phase 3

Fraud detection, instant payouts, and analytics dashboard.

---

## Prototype Demonstration

The prototype demonstrates:

* Risk prediction using environmental conditions
* Premium calculation using AI model
* Parametric disruption triggers
* Simulated claim payout
