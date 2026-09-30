# Artificial Intelligence Laboratory Assignments

## Student Information

| Field | Details |
|---|---|
| **Name** | Yash Singh |
| **Student ID** | 2024A7PS0617G |

This repository contains the solutions and implementation files for the five Artificial Intelligence laboratory assignments.

---

## Assignments

### 1. Logical Planning

**Topic:** Logical Reasoning for Planning

This assignment implements a simple planning agent for a warehouse robot using:

- States represented as logical propositions
- Action preconditions and effects
- Breadth-First Search (BFS)
- Plan generation and state transitions
- Validation of generated plans
- Tests for solvable, impossible, and irrelevant-action cases
- Reflection on using an LLM as an engineering assistant

**Key concepts:**
`Logic + Search → Planning`

**Folder:** `01_Logical_Planning/`

---

### 2. Search and A*

**Topic:** Search Algorithms and A* Search

This assignment implements and evaluates an A* search agent for warehouse navigation.

The work covers:

- Search problem formulation
- State, action, transition, goal, and cost definitions
- Grid-based warehouse navigation
- A* search with Manhattan-distance heuristic
- BFS comparison
- Path reconstruction
- States-expanded measurement
- Tests for trivial, impossible, and alternative-path cases
- Investigation of different heuristic functions
- Reflection on LLM-assisted implementation

**Key concepts:**
`BFS`, `A*`, `g(n)`, `h(n)`, `f(n) = g(n) + h(n)`

**Folder:** `02_Search_AStar/`

---

### 3. Goal-Based Agent

**Topic:** Goal-Based Intelligent Agents

This assignment constructs a goal-based agent for a warehouse navigation problem.

The work covers:

- Environment representation
- Current state
- Goal state
- Available actions
- Decision-making component
- Goal-based agent architecture
- Prompt engineering for generating the implementation
- Execution and testing of the generated Python program
- Reflection on the selected search strategy and LLM-assisted development

**Folder:** `03_Goal_Based_Agent/`

---

### 4. Neural Models

**Topic:** Learning, Depth, Activations, and Output Layers

This assignment investigates a small neural network using the XOR problem.

The implementation covers:

- XOR problem specification
- Linear separability
- A `2 → 2 → 1` neural network
- Nonlinear hidden activations
- Sigmoid output and binary classification
- Binary cross-entropy / `BCEWithLogitsLoss`
- Backpropagation and gradient inspection
- Symmetry caused by identical/zero weight initialization
- Comparison of sigmoid, tanh, and ReLU
- Three-class extension using softmax and cross-entropy
- Experimental validation and reflection on LLM-assisted engineering

**Key concepts:**
`Forward Pass`, `Backpropagation`, `Gradient`, `Activation Functions`, `Softmax`, `Cross-Entropy`

**Folder:** `04_Neural_Models/`

---

### 5. Bayesian Networks and Autoregressive Language Models

**Topic:** Bayesian Networks, Conditional Probability, and Autoregressive Language Models

This assignment connects Bayesian-network concepts with simple autoregressive language models.

The implementation includes:

- Chain-rule factorisation
- First-order Bayesian network / language model
- Conditional probability tables
- Transition counting
- Next-word prediction
- Greedy generation
- Probability-based sampling
- Probability-normalisation tests
- Second-order Bayesian network / language model
- Comparison of first-order and second-order models
- Generated text examples
- Reflection on LLM-assisted implementation and verification

**Key concepts:**
`Bayesian Networks`, `CPTs`, `Chain Rule`, `n-gram Models`, `Autoregressive Generation`

**Folder:** `05_Bayesian_Networks/`

---

## Repository Structure

```text
AI-Laboratory-Assignments/
│
├── README.md
│
├── 01_Logical_Planning/
│   ├── ...
│
├── 02_Search_AStar/
│   ├── ...
│
├── 03_Goal_Based_Agent/
│   ├── ...
│
├── 04_Neural_Models/
│   ├── ...
│
└── 08_Bayesian_Networks/
    ├── ...
```

The exact filenames inside each assignment folder may vary depending on the submitted implementation and report format.

---

## Technologies Used

- **Python 3**
- **NumPy**
- **PyTorch** — Neural Models assignment
- Python standard library data structures and random sampling
- Jupyter Notebook / Python IDE
- Large Language Models as engineering assistants

No pretrained language model or specialised machine-learning library is required for the Bayesian Networks laboratory implementation.

---

## Role of LLMs

The laboratories use Large Language Models as **engineering assistants**, rather than as replacements for understanding or verification.

The general workflow followed across the assignments is:

```text
Understand
    ↓
Specify
    ↓
Design
    ↓
Ask the LLM
    ↓
Implement
    ↓
Test
    ↓
Verify
    ↓
Reflect
```

The generated implementations are validated against the specifications through test cases, numerical checks, state transitions, probability normalisation, and experimental results.

---

## Learning Themes

Across the five assignments, the laboratories cover a progression of AI concepts:

```text
Logical Reasoning
       ↓
Search
       ↓
Goal-Based Agents
       ↓
Neural Models
       ↓
Probabilistic Models
       ↓
Autoregressive Language Models
```

The assignments also emphasise an important engineering principle:

> A program that runs is not necessarily a program that implements the intended AI model correctly.

Therefore, each assignment includes explicit testing, validation, or experimental analysis.

---

## Student

**Yash Singh**  
**Student ID:** `2024A7PS0617G`

