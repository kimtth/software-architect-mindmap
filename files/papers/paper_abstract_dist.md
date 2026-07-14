---
title: Distributed Systems Paper Abstracts and Study Notes
description: Technical and intuitive summaries for distributed systems papers
ms.date: 2026-07-14
---

## 70+ Distributed Systems Papers

### 38. Time, Clocks, and the Ordering of Events in a Distributed System

**Year:** 1978 | **Collection:** 70_plus_dist | [Source](https://lamport.azurewebsites.net/pubs/time-clocks.pdf) | [Local paper](70_plus_dist/001-time-clocks-and-the-ordering-of-events-in-a-distributed-system-1978.pdf)

#### Research Snapshot

Lamport defines causality with the happened-before relation and gives logical-clock rules that assign increasing timestamps to causally related events. The paper also shows how timestamp pairs impose a deterministic total order and analyzes synchronization of physical clocks.

#### Core Ideas

Lamport separates physical time from causality. The relation $a \rightarrow b$ means that event $a$ happened before event $b$: either both occurred in one process in program order, one was a message send and the other its receipt, or the relation follows transitively through other events. Each process carries a logical clock and advances it before an event; on receipt of timestamp $t$, it sets its clock to at least $t+1$. This makes causally ordered events receive increasing timestamps without requiring synchronized wall clocks.

#### Why It Matters and Impact

Distributed machines cannot observe a universal "now," yet they must reason about precedence, debugging traces, mutual exclusion, and replicated updates. The happened-before relation supplies that vocabulary, while Lamport clocks turn it into a distributed procedure. The paper established logical time as a foundational abstraction and led directly to timestamp-based ordering techniques, including vector clocks for detecting concurrency.

#### Key Formulas or Algorithms

For any event $a$ and $b$, $a \rightarrow b$ holds when $a$ precedes $b$ locally, $a$ sends a message received by $b$, or there is an event $c$ such that $a \rightarrow c \rightarrow b$. Maintain clock $C_i$ at process $i$: before each event set $C_i \leftarrow C_i+1$; send $C_i$ with every message; after receiving timestamp $t$, set $C_i \leftarrow \max(C_i,t)+1$. Then $a \rightarrow b$ implies $C(a)\lt C(b)$. A total order breaks equal timestamps with process identifiers: $a \Rightarrow b$ when $(C(a),i_a)$ is lexicographically smaller than $(C(b),i_b)$.

#### Intuition

Each process owns a logical counter, increments it before every local event, and attaches its current counter value to every sent message. On receipt of timestamp $t$, the receiving process sets its counter to $\max(\text{local},t)+1$ before recording the receive event; therefore a causal send-to-receive chain always has increasing timestamps, although equal timestamps can still describe concurrent events and need a process identifier only for a deterministic total order.

#### Main Takeaway

Correct distributed ordering begins with causality, not synchronized clocks: logical timestamps preserve what can be known about which events influenced others.

### 39. QuePaxa: Escaping the Tyranny of Timeouts in Consensus

**Year:** 2023 | **Collection:** 70_plus_dist | [Source](https://discovery.ucl.ac.uk/10181480/1/quepaxa.pdf) | [Local paper](70_plus_dist/002-quepaxa-escaping-the-tyranny-of-timeouts-in-consensus-2023.pdf)

#### Research Snapshot

QuePaxa combines a randomized asynchronous consensus core with a one-round-trip fast path. Replicas may hedge concurrent proposals after short adaptive delays, and a bandit policy selects leaders and delays, so liveness does not depend on declaring a leader failed after a fixed timeout.

#### Core Ideas

QuePaxa combines an asynchronous randomized consensus core with a one-round-trip fast path. Unlike Multi-Paxos and Raft, it does not need a timeout to decide that a leader has failed before it can make progress. Multiple replicas may propose concurrently, and the protocol prevents those proposals from destructively colliding. In the common case, a selected leader drives the fast path; a multi-armed-bandit policy learns which leader and short hedging delay work best under current network conditions.

#### Why It Matters and Impact

Timeouts trade speed for safety of operation: conservative values delay real failures, while aggressive values create unnecessary view changes during a slow network or a denial-of-service attack. QuePaxa targets that liveness weakness without abandoning normal-case efficiency. Its prototype reaches throughput comparable to Multi-Paxos in LAN and WAN experiments while remaining live under attacks, misconfiguration, and slow leaders that can stall timeout-driven systems.

#### Key Formulas or Algorithms

For each candidate leader $k$, QuePaxa treats the observed completion reward as an arm in a bandit problem and selects the leader and hedge delay that maximize expected reward. Operationally: propose on the fast path; after hedge delay $h$, issue a redundant proposal rather than wait for a fixed failure timeout; collect the protocol's quorum evidence; and use the randomized asynchronous core when concurrency or adverse timing prevents fast-path completion. The delay $h$ is an adaptive performance parameter, not a correctness assumption, so missing timing bounds cannot stop eventual progress.

#### Intuition

Replicas first try to decide a client value through a selected leader's one-round-trip path, but a short learned hedge can start another proposal when that attempt is slow instead of waiting to declare the leader dead. Quorum certificates and the asynchronous randomized agreement core ensure conflicting proposals cannot both decide; the bandit-chosen leader and hedge delay affect latency only, while randomized progress avoids making a timeout bound a liveness requirement.

#### Main Takeaway

QuePaxa decouples consensus liveness from failure-detection timeouts while retaining a leader-like fast path for efficient ordinary operation.

### 40. Graham: Synchronizing Clocks by Leveraging Local Clock Properties

**Year:** 2022 | **Collection:** 70_plus_dist | [Source](https://www.usenix.org/system/files/nsdi22-paper-najafi_1.pdf) | [Local paper](70_plus_dist/003-graham-synchronizing-clocks-by-leveraging-local-clock-properties-2019.pdf)

#### Research Snapshot

Graham synchronizes distributed clocks by exploiting measured local-clock behavior rather than assuming ideal clocks. It models each clock’s offset and rate within local uncertainty bounds, exchanges time information, and computes corrections that reduce global skew while preserving stated clock assumptions.

#### Core Ideas

Graham observes that much of a commodity quartz clock's frequency error is either stable, such as manufacturing tolerance and aging, or predictably temperature-dependent. It learns a machine-specific temperature-to-frequency-error curve from normal NTP, PTP, or PPS synchronization observations and readings from existing server sensors. The resulting correction lets the local clock remain useful during missed synchronizations instead of treating every loss of the remote reference as an immediate synchronization failure.

#### Why It Matters and Impact

Sub-microsecond clock bounds matter to strongly consistent distributed systems because timestamp uncertainty can force operations to wait. Conventional designs conservatively assume $200\ \mathrm{ppm}$ drift, requiring frequent synchronization and making a missed update costly. Graham shows that software can characterize and compensate commodity clocks to achieve roughly $100\ \mathrm{ppb}$ stability in typical experiments, reducing drift by up to $2000\times$ without specialized timing hardware and extending the period over which a synchronized clock can safely operate alone.

#### Key Formulas or Algorithms

The holdover time for an allowed uncertainty $\epsilon$ and residual frequency drift $d_f$ is $t_h=\epsilon/d_f$. Graham models temperature-dependent relative frequency error as $\Delta f_T=k_0+k_1T+k_2T^2+k_3T^3$. From synchronization intervals, it derives observations $\Delta f\,\Delta t_{si}=\Delta t_{so}-\Delta t_{si}$, then solves the accumulated linear system for $k_0,\ldots,k_3$ by least squares. It samples candidate sensors, retains bounded recent observations, applies corrections only after the learned curve is sufficiently accurate, and chooses sensors whose curves minimize residual frequency error.

#### Intuition

Each host observes its local oscillator's temperature and its offset from NTP, PTP, or PPS updates, then learns a machine-specific temperature-to-frequency-error curve. During a missed reference update it advances time using that correction and a residual-error bound, so its uncertainty grows slowly rather than at a pessimistic generic drift rate; the safety tradeoff is that corrections are used only after enough observations make the bound trustworthy.

#### Main Takeaway

Commodity clocks are substantially more predictable than conservative drift bounds imply: learning and compensating each machine's local temperature-dependent behavior can preserve microsecond-scale synchronization through missed updates.

### 41. Megatron-LM: Training Multi-Billion Parameter Language Models Using Model Parallelism

**Year:** 2018 | **Collection:** 70_plus_dist | [Source](https://arxiv.org/pdf/1909.08053) | [Local paper](70_plus_dist/004-megatron-lm-training-multi-billion-parameter-language-models-using-model-2018.pdf)

#### Research Snapshot

Megatron-LM trains multi-billion-parameter Transformers by partitioning attention heads and feed-forward matrix operations across GPUs. Carefully placed collective communication reconstructs layer outputs, allowing tensor parallelism to combine with other parallel training techniques in PyTorch.

#### Core Ideas

Megatron-LM trains billion-parameter Transformers by splitting individual matrix operations across GPUs. It partitions attention heads and feed-forward hidden units, then uses a small number of collective communications to reassemble each layer's result.

#### Why It Matters and Impact

The approach made model parallelism practical in ordinary PyTorch rather than a specialized compiler. It demonstrated 8.3-billion-parameter GPT-2-like training on 512 GPUs with strong scaling efficiency and influenced later tensor-parallel training stacks.

#### Key Formulas or Algorithms

For a column-parallel linear layer, each GPU computes $Y_i=XA_i$ and the following row-parallel layer computes $Z=\sum_i Y_iB_i$. The first split needs no communication; the second uses an all-reduce. Attention heads are split similarly, with $\mathrm{softmax}(QK^\top/\sqrt{d_k})V$ computed independently per head.

#### Intuition

For each Transformer layer, GPUs hold disjoint attention heads or matrix-column slices, compute their local activations in parallel, and use an all-reduce only where the next row-parallel operation needs their summed contribution. The partition preserves exactly the dense layer and attention mathematics, while minimizing synchronization: communication occurs at layer boundaries rather than moving every parameter or activation to every GPU.

#### Main Takeaway

Careful intra-layer partitioning can train very large Transformers efficiently without changing their mathematical architecture.

### 42. SDPipe: A Semi-Decentralized Framework for Heterogeneity-Aware Pipeline-Parallel Training

**Year:** 2023 | **Collection:** 70_plus_dist | [Source](https://www.vldb.org/pvldb/vol16/p2354-miao.pdf) | [Local paper](70_plus_dist/005-sdpipe-a-semi-decentralized-framework-for-heterogeneity-aware-pipeline-parallel-2023.pdf)

#### Research Snapshot

SDPipe targets pipeline-parallel training on heterogeneous cloud workers. It decentralizes high-volume model synchronization within groups, while a lightweight controller uses global measurements to form and reschedule groups that avoid slow stages.

#### Core Ideas

SDPipe separates two decisions that react differently to heterogeneity. Workers decentralize costly model synchronization within pipeline groups, while a central controller performs lightweight group scheduling using its global view of changing worker speed.

#### Why It Matters and Impact

Cloud training clusters are neither dedicated nor homogeneous. SDPipe avoids both a parameter-server bottleneck and all-reduce's tendency to wait for stragglers, improving throughput and convergence behavior in volatile environments.

#### Key Formulas or Algorithms

It forms pipeline groups from workers with compatible measured throughput, assigns data-parallel replicas to groups, and synchronizes a group's model through decentralized communication. The scheduler periodically remaps stages when estimated iteration time $T\approx\max_s T_s$ reveals an imbalanced stage.

#### Intuition

The controller measures worker speed and network conditions, groups compatible workers into pipeline replicas, and assigns model stages so no stage dominates iteration time. Within each group workers exchange high-volume model state without a central parameter-server bottleneck; when a worker becomes slow or conditions change, the controller reschedules groups, trading occasional reconfiguration for steadier throughput and less straggler waiting.

#### Main Takeaway

Hybrid control is effective when global scheduling needs a system-wide view but high-volume synchronization must avoid a central bottleneck.

### 43. The Power of Two Choices in Randomized Load Balancing

**Year:** 2001 | **Collection:** 70_plus_dist | [Source](https://www.eecs.harvard.edu/~michaelm/postscripts/tpds2001.pdf) | [Local paper](70_plus_dist/006-the-power-of-two-choices-in-randomized-load-balancing-2001.pdf)

#### Research Snapshot

The paper analyzes the supermarket model, where each arrival samples $d$ random queues and joins the shortest. A mean-field limit predicts equilibrium delays and shows that two choices give an exponential improvement over one, whereas further choices give diminishing returns.

#### Core Ideas

In the supermarket model, each arrival samples $d$ random queues and joins the shortest sampled queue. The paper analyzes the equilibrium of this policy as the number of servers grows.

#### Why It Matters and Impact

Two probes deliver an exponential improvement in delay over one random choice, while a third gives only a constant-factor improvement over two. This result motivated the ubiquitous power-of-two-choices policy in load balancers, hash tables, and schedulers.

#### Key Formulas or Algorithms

Let $q_i$ be the fraction of queues with length at least $i$. In the mean-field limit, $q_{i+1}=\lambda q_i^d$, hence $q_i=\lambda^{(d^i-1)/(d-1)}$. Route every arriving job to $\arg\min_{j\in\{s_1,\ldots,s_d\}}\ell_j$.

#### Intuition

When a job arrives, it samples $d$ random servers, reads their queue lengths, and joins the least loaded sampled queue. A queue can become very long only if all sampled alternatives are already long, so for two choices that bad event is squared at each level; the extra probe cost buys a dramatically smaller tail of queueing delay, whereas additional choices give smaller marginal gains.

#### Main Takeaway

A tiny amount of choice information dramatically improves randomized load balancing.

### 44. Karma: Resource Allocation for Dynamic Demands

**Year:** 2023 | **Collection:** 70_plus_dist | [Source](https://www.usenix.org/system/files/osdi23-vuppalapati.pdf) | [Local paper](70_plus_dist/007-karma-resource-allocation-for-dynamic-demands-2023.pdf)

#### Research Snapshot

Karma allocates shared capacity when tenant demand changes over time. Tenants receive credits for unused resources they make available and spend credits when borrowing beyond their current share; priority by accumulated credit preserves dynamic fairness while keeping capacity productive.

#### Core Ideas

Karma extends max-min fairness to tenants whose demands change over time. A tenant earns credits by donating unused capacity and spends credits when borrowing capacity above its current fair share.

#### Why It Matters and Impact

Static max-min fairness can reward a tenant that transiently demands capacity while ignoring another tenant's earlier donation. Karma carries that history forward, preserving efficiency, incentives, and low performance disparity under dynamic demand.

#### Key Formulas or Algorithms

At each allocation quantum, give each user its demanded share when possible; record donated units as credit and debit borrowed units. Allocate scarce residual capacity in descending credit order, subject to $\sum_i a_i\le C$. Credits encode past net contribution.

#### Intuition

At every allocation interval Karma compares each tenant's demand with its fair share: unused offered capacity earns the tenant credits, and capacity borrowed above share spends them. When demand exceeds capacity, it serves feasible baseline demand and grants the scarce excess in credit order, preserving the invariant that a tenant which previously helped utilization is not disadvantaged when it later needs capacity.

#### Main Takeaway

Resource fairness over time requires accounting for both present demand and past cooperation.

### 45. SelfTune: Tuning Cluster Managers

**Year:** 2023 | **Collection:** 70_plus_dist | [Source](https://www.usenix.org/system/files/nsdi23-karthikeyan.pdf) | [Local paper](70_plus_dist/008-selftune-tuning-cluster-managers-2023.pdf)

#### Research Snapshot

SelfTune integrates online reinforcement learning into iterative cluster managers. Developers expose tunable parameters and performance feedback, allowing the system to safely adjust settings as workloads and cluster conditions change in production.

#### Core Ideas

SelfTune embeds reinforcement learning into iterative cluster managers to tune their exposed parameters online. Developers provide a small interface, and the framework observes state, chooses a parameter action, and receives a performance reward after the manager advances the cluster.

#### Why It Matters and Impact

Operator-selected constants age badly as workload and hardware conditions change. Deployed across tens of thousands of machines, SelfTune improved throughput by up to 20 percent by continuously adjusting job concurrency.

#### Key Formulas or Algorithms

The controller learns a policy $\pi(a\mid s)$ over tuning actions $a$ from cluster state $s$, maximizing discounted reward $\mathbb{E}[\sum_t\gamma^t r_t]$. It uses safe, incremental parameter changes so normal cluster-manager iterations remain the mechanism that applies actions.

#### Intuition

The existing cluster-manager loop exposes a state, bounded tuning knobs, and a measured reward such as throughput; SelfTune chooses a small parameter change, lets the normal manager apply it, and observes the next outcome. Its learner explores only safe incremental actions and favors settings with better long-run reward, so adaptation follows workload changes without replacing the manager's correctness-critical scheduling logic.

#### Main Takeaway

Production control parameters can be learned continuously when tuning is integrated with an existing iterative control loop.

### 46. MapReduce: Simplified Data Processing on Large Clusters

**Year:** 2004 | **Collection:** 70_plus_dist | [Source](https://static.googleusercontent.com/media/research.google.com/en//archive/mapreduce-osdi04.pdf) | [Local paper](70_plus_dist/009-mapreduce-simplified-data-processing-on-large-clusters-2004.pdf)

#### Research Snapshot

MapReduce provides a programming model in which map functions emit intermediate key-value pairs and reduce functions combine values for each key. Its runtime partitions input, schedules tasks near data, shuffles grouped intermediate records, and re-executes failed or slow tasks.

#### Core Ideas

MapReduce lets programmers express a large job as `map` functions producing intermediate key-value pairs and `reduce` functions merging all values for one key. The runtime handles partitioning, placement, retries, and shuffle communication.

#### Why It Matters and Impact

It made cluster-scale batch processing accessible without requiring every program to implement distributed scheduling and fault recovery. The abstraction became a template for Hadoop and later dataflow engines.

#### Key Formulas or Algorithms

$\mathrm{map}(k_1,v_1)\rightarrow[(k_2,v_2)]$ and $\mathrm{reduce}(k_2,[v_2])\rightarrow[(k_3,v_3)]$. Hash-partition intermediate keys to reducers, execute map tasks near input blocks, and re-execute failed or straggling tasks speculatively before committing one output.

#### Intuition

Map tasks read independent input splits and emit intermediate $(key,value)$ records; the runtime partitions those records by key, transfers each partition to one reduce task, sorts or groups equal keys, and invokes the user's reducer. A master records task completion and re-executes failed or slow attempts, committing one output per task, so the programmer supplies deterministic transformations while the runtime absorbs placement, failure, and straggler handling.

#### Main Takeaway

Restricting distributed computation to map, shuffle, and reduce moves most operational complexity from application code into a reusable runtime.

### 47. Apache Hadoop YARN: Yet Another Resource Negotiator

**Year:** 2013 | **Collection:** 70_plus_dist | [Source](https://www.cse.ust.hk/~weiwa/teaching/Fall15-COMP6611B/reading_list/YARN.pdf) | [Local paper](70_plus_dist/010-apache-hadoop-yarn-yet-another-resource-negotiator-2013.pdf)

#### Research Snapshot

YARN separates Hadoop resource management from application execution. A cluster-wide ResourceManager grants containers, node agents manage local resources, and an ApplicationMaster controls one application’s tasks, retries, and execution model.

#### Core Ideas

YARN decouples Hadoop's resource management from MapReduce execution. A global ResourceManager allocates containers, NodeManagers manage each host, and an ApplicationMaster coordinates one application's tasks and recovery.

#### Why It Matters and Impact

The split lets one shared Hadoop cluster run multiple programming models rather than forcing every workload into MapReduce. It removes centralized job-control pressure while preserving centralized resource arbitration.

#### Key Formulas or Algorithms

An application requests container resources $(m,v)$, typically memory and virtual cores. The scheduler grants containers under capacity and queue policies; the ApplicationMaster then launches tasks, monitors them, and asks for replacements after failures.

#### Intuition

An application submits resource needs to the cluster ResourceManager, which grants containers according to global capacity and queue policy; NodeManagers enforce each container's local limits. The application's own ApplicationMaster then launches, monitors, and retries its tasks in those containers, so centralized arbitration remains fair while application-specific execution and recovery do not overload one global scheduler.

#### Main Takeaway

Separating shared resource allocation from application-specific control makes a cluster platform more scalable and extensible.

### 48. Pregel: A System for Large-Scale Graph Processing

**Year:** 2010 | **Collection:** 70_plus_dist | [Source](https://kowshik.github.io/JPregel/pregel_paper.pdf) | [Local paper](70_plus_dist/011-pregel-a-system-for-large-scale-graph-processing-2010.pdf)

#### Research Snapshot

Pregel expresses graph algorithms as bulk-synchronous supersteps. Each active vertex consumes prior-round messages, changes local graph state, emits messages for the next round, and may halt; the system supplies barriers, partitioning, and recovery.

#### Core Ideas

Pregel exposes graph computation as bulk synchronous parallel supersteps. Active vertices receive messages from the prior step, update local vertex or edge state, send messages, and vote to halt; the system synchronizes at each barrier.

#### Why It Matters and Impact

The vertex-centric model hides partitioning and recovery while directly expressing algorithms such as PageRank, shortest paths, and connectivity. It established the model used by many graph-processing systems.

#### Key Formulas or Algorithms

In superstep $s$, invoke $\mathrm{Compute}(v,M_v^{s-1})$ and deliver all emitted messages in $s+1$. PageRank illustrates the pattern: $r_v^{s+1}=(1-d)/N+d\sum_{u\to v}r_u^s/\deg^+(u)$.

#### Intuition

In a superstep, every active vertex receives the messages produced for it in the previous superstep, updates only its local vertex or edge state, and sends messages that become visible at the next barrier. A vertex can vote to halt, but wakes if a later message arrives; the barrier makes each round's state well defined and lets the system recover partitions without exposing asynchronous message races to graph algorithms.

#### Main Takeaway

Synchronous message-passing gives large graph algorithms a simple, fault-tolerant distributed execution model.

### 49. Chaos: Scale-Out Graph Processing from Secondary Storage

**Year:** 2015 | **Collection:** 70_plus_dist | [Source](https://sigops.org/s/conferences/sosp/2015/current/2015-Monterey/089-roy-online.pdf) | [Local paper](70_plus_dist/012-chaos-scale-out-graph-processing-from-secondary-storage-2015.pdf)

#### Research Snapshot

Chaos processes disk-resident graphs across a cluster using streaming partitions designed for sequential I/O. It distributes graph data uniformly instead of pursuing locality and uses work stealing so multiple machines can finish an uneven partition.

#### Core Ideas

Chaos scales X-Stream-style streaming graph partitions across machines with disks. It partitions for sequential I/O rather than graph locality, randomly distributes data, and steals work so several machines can process an imbalanced partition.

#### Why It Matters and Impact

For trillion-edge graphs, aggregate disk capacity and bandwidth matter more than perfect graph placement. Chaos showed that on small clusters the network can be faster than storage, overturning locality-first assumptions.

#### Key Formulas or Algorithms

Edges are streamed sequentially through scatter and gather phases. A worker that finishes its assigned partition obtains unprocessed chunks from another worker; runtime balance targets $T\approx\max_i\{\text{remaining I/O work}_i\}/B_{\text{aggregate}}$.

#### Intuition

Workers stream edge partitions sequentially from local disks through scatter and gather phases, producing updates without requiring random graph access. Data is deliberately spread so every machine can contribute storage bandwidth, and an idle worker steals an unfinished chunk from a slow owner; this sacrifices strict locality but prevents skew from leaving disks and CPUs idle.

#### Main Takeaway

Sequential storage access plus work stealing can outperform expensive locality-oriented preprocessing for out-of-core graph analytics.

### 50. Scalability! But at What COST?

**Year:** 2014 | **Collection:** 70_plus_dist | [Source](https://www.usenix.org/system/files/conference/hotos15/hotos15-paper-mcsherry.pdf) | [Local paper](70_plus_dist/013-scalability-but-at-what-cost-2014.pdf)

#### Research Snapshot

COST measures the smallest parallel configuration that outperforms a competent single-thread implementation on the same workload. The metric exposes fixed overheads that conventional scaling curves can hide.

#### Core Ideas

COST measures the smallest parallel hardware configuration that beats a competent single-threaded implementation on the same problem. It exposes fixed distributed-system overheads that conventional speedup curves hide.

#### Why It Matters and Impact

A system can scale with additional cores yet still be slower than one thread at every reported size. COST shifted evaluation toward meaningful baselines and encouraged authors to quantify the price of distribution.

#### Key Formulas or Algorithms

For platform $P$, $\mathrm{COST}(P)=\min\{n:T_P(n)\lt T_{\text{single}}(1)\}$. Measure the single-thread baseline, run the distributed system at increasing core counts, and report the first $n$ that crosses that threshold.

#### Intuition

First implement and measure a competent single-thread baseline on the same input, then run the parallel system with increasing worker counts and find the smallest count whose elapsed time is lower. That crossing point is COST: it exposes fixed costs for serialization, communication, scheduling, and data movement that a relative speedup curve can hide, so adding workers is meaningful only after they repay those costs.

#### Main Takeaway

Scalability claims need a strong serial baseline and an explicit accounting of parallel overhead.

### 51. Storm@Twitter

**Year:** 2014 | **Collection:** 70_plus_dist | [Source](https://cs.brown.edu/courses/csci2270/archives/2015/papers/ss-storm.pdf) | [Local paper](70_plus_dist/014-storm-twitter-2014.pdf)

#### Research Snapshot

Storm is a fault-tolerant streaming system that executes topologies of tuple sources and processing operators. It assigns components across workers and tracks each emitted tuple tree with XOR-based acknowledgments, replaying roots that do not complete.

#### Core Ideas

Storm executes a streaming topology of spouts that emit tuples and bolts that transform them. Nimbus assigns work, Supervisors run workers, and tuple trees track acknowledgments to provide at-least-once processing.

#### Why It Matters and Impact

Twitter used Storm for real-time critical computations, demonstrating operational patterns for low-latency stream processing at production scale. Its topology abstraction shaped later streaming platforms.

#### Key Formulas or Algorithms

For a spout tuple root, Storm assigns a random XOR identifier. Each emitted descendant XORs its edge value into an ack; when the root's accumulated XOR becomes zero, the tuple is complete. A timeout triggers replay if the root is not fully acknowledged.

#### Intuition

For each spout tuple, Storm assigns a root identifier and tracks the directed tree of tuples emitted by bolts; acknowledgments XOR edge identifiers into the root's accumulator. When every descendant has acknowledged, the accumulator returns to zero and the root is complete; if the timeout expires first, Storm replays the root, giving at-least-once processing while avoiding one coordinator record for every tree edge.

#### Main Takeaway

Storm combines a simple streaming DAG with distributed acknowledgment tracking to make failure recovery practical for continuous computation.

### 52. A Survey of Distributed Data Stream Processing Frameworks

**Year:** 2019 | **Collection:** 70_plus_dist | [Source](https://ieeexplore.ieee.org/ielx7/6287639/8600701/08864052.pdf) | [Local paper](70_plus_dist/015-a-survey-of-distributed-data-stream-processing-frameworks-2019.pdf)

#### Research Snapshot

This survey classifies distributed stream-processing frameworks by execution model, latency, state, windows, fault tolerance, and delivery semantics. It compares representative open-source and commercial systems and relates their design choices to application requirements.

#### Core Ideas

The survey classifies stream processors by dataflow model, processing semantics, windowing, fault tolerance, latency, and deployment model. It compares Storm, Spark Streaming, Flink, Kafka Streams, IBM Streams, and a multilevel analytics architecture.

#### Why It Matters and Impact

Stream frameworks make different trade-offs between per-record latency, replayable state, throughput, and exactly-once guarantees. The taxonomy turns product selection into a requirements-matching exercise rather than a brand comparison.

#### Key Formulas or Algorithms

For a time window $W=[t-W,t)$, an aggregation maintains $A_W=\bigoplus_{e:t_e\in W}v_e$. Micro-batching processes intervals $\Delta$, whereas record-at-a-time engines update state per event; both must coordinate checkpoints and offsets to recover consistently.

#### Intuition

An incoming event triggers either immediate record-at-a-time state updates or inclusion in a micro-batch; operators then group events by processing or event-time windows and maintain state. Recovery coordinates source offsets with checkpoints or replay, so the important choice is whether the workload needs low per-record latency, event-time correctness, stateful recovery, and at-least-once or exactly-once effects, not merely maximum throughput.

#### Main Takeaway

The correct stream processor follows the workload's latency, state, event-time, and delivery-semantics requirements.

### 53. Dashlet: Taming Swipe Uncertainty for Robust Short Video Streaming

**Year:** 2023 | **Collection:** 70_plus_dist | [Source](https://www.usenix.org/system/files/nsdi23-li-zhuqi.pdf) | [Local paper](70_plus_dist/016-dashlet-taming-swipe-uncertainty-for-robust-short-video-streaming-2023.pdf)

#### Research Snapshot

Dashlet improves short-video playback by predicting which item and chunks a viewer is likely to watch after a swipe. It prebuffers selected chunks out of presentation order and chooses bitrates using swipe statistics and available bandwidth.

#### Core Ideas

Dashlet prebuffers chunks for short-video feeds out of order. It models swipe timing and direction from user measurements, then prioritizes a chunk's probability of being watched against its bitrate and expected download time.

#### Why It Matters and Impact

Linear-video buffering assumes viewers consume the next segment. Swipe feeds invalidate that assumption, causing stalls or wasted downloads. Dashlet improved quality of experience while reducing unseen bytes by about 30 percent.

#### Key Formulas or Algorithms

For candidate chunk $c$, prioritize expected utility $U(c)=P(\text{watch }c)\cdot Q(c)-\lambda\,P(\text{skip }c)\cdot S(c)$. Recompute candidate order after each swipe and choose a bitrate that fits predicted throughput before the candidate's likely playback deadline.

#### Intuition

After each swipe, the client uses observed swipe direction and dwell-time probabilities to rank chunks from the current and likely next videos by expected viewing value. It fetches the most likely near-deadline chunks first and selects a bitrate that predicted bandwidth can finish in time; this trades some speculative bytes for fewer visible stalls and avoids spending bandwidth on clips the viewer will skip.

#### Main Takeaway

Short-video streaming needs prediction-aware, out-of-order prefetching rather than linear playback buffering.

### 54. The Emergence of Edge Computing

**Year:** 2013 | **Collection:** 70_plus_dist | [Source](https://doi.org/10.1109/MC.2017.9) | [Local paper](70_plus_dist/017-the-emergence-of-edge-computing-2013.pdf)

#### Research Snapshot

The paper argues for edge computing, which places compute and storage close to mobile devices and sensors while retaining the cloud for centralized scale. Nearby nodes can reduce interaction latency, enforce local policy, exploit context, and mask short cloud disconnections.

#### Core Ideas

Edge computing places cloudlet-like compute and storage near mobile devices and sensors, complementing centralized clouds. It targets responsive interaction, local context, privacy enforcement, and tolerance of transient cloud disconnection.

#### Why It Matters and Impact

The paper articulated why centralized cloud economics cannot satisfy every mobile and IoT workload. It framed the edge as a tier in a continuum, influencing cloudlet, fog, and modern edge-platform designs.

#### Key Formulas or Algorithms

Offloading is useful when $T_{\text{edge}}+T_{\text{network}}\lt T_{\text{device}}$ and the energy cost is acceptable. Placement weighs latency, bandwidth, privacy constraints, and device mobility; state may be cached or migrated between nearby edge nodes.

#### Intuition

An application places latency-sensitive computation or data filtering on a nearby cloudlet or edge node when device-to-edge delay, bandwidth, privacy, or intermittent cloud connectivity makes a distant service unsuitable. It sends compact results or nonurgent work to the central cloud, so the practical tradeoff is local responsiveness and context against the cloud's larger shared capacity and simpler global management.

#### Main Takeaway

Distributing selected cloud capabilities near data sources addresses latency, mobility, privacy, and disconnection that centralization alone cannot solve.

### 55. A Survey of Fog Computing: Concepts, Applications and Issues

**Year:** 2015 | **Collection:** 70_plus_dist | [Source](https://www.cs.wm.edu/~liqun/paper/mobidata15-fog.pdf) | [Local paper](70_plus_dist/018-a-survey-of-fog-computing-concepts-applications-and-issues-2015.pdf)

#### Research Snapshot

This survey defines fog computing as a distributed resource layer between end devices and centralized clouds. It compares related concepts, reviews IoT applications, and identifies challenges in placement, mobility, heterogeneity, management, security, and privacy.

#### Core Ideas

The survey defines fog computing as elastic compute, storage, and networking resources between end devices and the cloud. It distinguishes fog from closely related edge and mobile-cloud concepts and reviews applications such as smart cities, vehicles, and healthcare.

#### Why It Matters and Impact

Fog is not merely a smaller cloud: it must manage geographic distribution, mobility, heterogeneous ownership, and local context. The survey organizes the design issues that later fog platforms must solve.

#### Key Formulas or Algorithms

Placement minimizes an objective such as $\alpha\,\text{latency}+\beta\,\text{energy}+\gamma\,\text{cost}$ subject to capacity, mobility, and privacy constraints. Typical control loops discover nearby nodes, place components, monitor quality, and migrate or scale them as conditions change.

#### Intuition

Sensors and mobile clients send work to geographically nearby fog nodes, which can filter data, make local decisions, or cache state before forwarding selected data to cloud services. A controller must choose and migrate placements as users move, capacity changes, or privacy boundaries apply; the benefit is lower latency and traffic, while the cost is managing heterogeneous, independently located resources.

#### Main Takeaway

Fog computing broadens cloud design with location-aware, distributed resource management for IoT and mobile applications.

### 56. Orbital Edge Computing: Nanosatellite Constellations as a New Class of Computer System

**Year:** 2020 | **Collection:** 70_plus_dist | [Source](https://brandonlucia.com/pubs/oec-asplos2020.pdf) | [Local paper](70_plus_dist/019-orbital-edge-computing-nanosatellite-constellations-as-a-new-class-of-computer-2020.pdf)

#### Research Snapshot

Orbital Edge Computing moves processing from ground stations onto sensor-equipped nanosatellites. A runtime predicts orbital contact, energy, and geography to schedule sensing and distributed pipeline stages when downlinking raw data is impractical.

#### Core Ideas

Orbital Edge Computing replaces the bent-pipe model, which downlinks raw satellite data for ground processing, with local satellite computation. A runtime predicts orbit, energy, and contact opportunities and organizes satellites into geography-driven pipelines without cross-links.

#### Why It Matters and Impact

Growing constellations are limited by downlink windows, antenna capacity, and solar energy. Processing data in orbit reduces required ground infrastructure and turns a satellite fleet into a constrained distributed computer.

#### Key Formulas or Algorithms

For each satellite, predict contact windows $C(t)$ and battery energy $E(t+1)=E(t)+H(t)-P(t)$. Schedule sensing and pipeline stages only when energy and orbital visibility permit; forward compact processed results during available downlinks.

#### Intuition

Each nanosatellite has sensors, compute, a finite battery, and predicted windows in which it can see a ground station or relevant geography. The runtime schedules sensing and pipeline stages only when energy reserve and future contact permit, keeps intermediate state on satellites as needed, and downlinks compact derived results during a contact; this replaces raw-data downlink demand with constrained in-orbit computation.

#### Main Takeaway

Orbit and energy are first-class scheduling constraints when satellites perform edge computation.

### 57. A Networking Perspective on Starlink's Self-Driving LEO Mega-Constellation

**Year:** 2023 | **Collection:** 70_plus_dist | [Source](https://dl.acm.org/doi/pdf/10.1145/3570361.3592519) | [Local paper](70_plus_dist/020-a-networking-perspective-on-starlink-s-self-driving-leo-mega-constellation-2023.pdf)

#### Research Snapshot

The study infers Starlink’s autonomous station keeping, collision avoidance, and shell-transfer maneuvers from public orbital data. It then measures how those maneuvers alter inter-satellite links, topology stability, routing, and higher-layer network behavior.

#### Core Ideas

The paper infers Starlink's autonomous orbit operations from public space-situational-awareness data. It characterizes station keeping, collision avoidance, and shell transfers, then examines their effects on inter-satellite-link topology and network operations.

#### Why It Matters and Impact

LEO motion is not a fixed routing substrate. Autonomous maneuvers can alter link availability and path stability, so constellation flight control and network control must be co-designed rather than treated independently.

#### Key Formulas or Algorithms

It reconstructs orbital trajectories from time-stamped element sets and detects maneuvers from deviations in altitude, inclination, and orbital plane. A link graph $G(t)=(V,E(t))$ then yields time-varying path properties such as reachability, hop count, and latency.

#### Intuition

Public orbital measurements reveal each satellite's nominal path and deviations caused by station keeping, collision avoidance, or shell transfers. Those motions change which inter-satellite links can exist and therefore change routes, hops, and delay over time; network control must predict the flight-control-driven topology rather than treating a scheduled constellation as a static graph.

#### Main Takeaway

Network performance in mega-constellations depends on the autonomous orbital behavior that continuously changes the topology.

### 58. Amalgamated Intermittent Computing Systems

**Year:** 2023 | **Collection:** 70_plus_dist | [Source](https://arxiv.org/pdf/2303.13000) | [Local paper](70_plus_dist/021-amalgamated-intermittent-computing-systems-2023.pdf)

#### Research Snapshot

Amalgamated intermittent computing coordinates several energy-harvesting devices as one logical system. It distributes work, communication, and durable state across nodes whose individual execution repeatedly stops when harvested energy runs out.

#### Core Ideas

Amalgamated intermittent computing treats multiple energy-harvesting devices as one logical system. It coordinates their intermittent execution, communication, and storage so a task can continue despite individual devices repeatedly losing power.

#### Why It Matters and Impact

Single intermittent devices are constrained by tiny energy buffers and frequent brownouts. Pooling devices creates larger effective energy and compute capacity while retaining energy-harvesting deployment benefits.

#### Key Formulas or Algorithms

Each node alternates between charged and unavailable states; a scheduler assigns work only when predicted energy $E_i$ exceeds task demand $e_j$ plus recovery reserve. Durable checkpoints preserve task progress across power failures and migrations.

#### Intuition

Each energy-harvesting node repeatedly charges, runs briefly, and may lose power before completing a task, so useful state is checkpointed in nonvolatile storage. The system assigns or migrates a task fragment to a node whose predicted energy covers execution plus recovery reserve, and coordinates messages and durable dependencies so a brownout causes replay from a known state rather than duplicate or lost effects.

#### Main Takeaway

Coordination can turn unreliable, energy-intermittent nodes into a more capable collective computing substrate.

### 59. A View of Cloud Computing

**Year:** 2010 | **Collection:** 70_plus_dist | [Source](https://people.eecs.berkeley.edu/~adj/publications/paper-files/p50-armbrust.pdf) | [Local paper](70_plus_dist/022-a-view-of-cloud-computing-2010.pdf)

#### Research Snapshot

The paper defines cloud computing through on-demand elasticity and economies of scale, then identifies major adoption opportunities and obstacles. It distinguishes service layers and frames availability, data transfer, lock-in, and unpredictable performance as central challenges.

#### Core Ideas

The paper defines cloud computing through elastic, on-demand resources and outlines its economics, opportunities, and obstacles. It distinguishes infrastructure, platform, and software services and identifies ten technical challenges, including availability, data transfer, and lock-in.

#### Why It Matters and Impact

It provided a durable vocabulary for cloud computing and explained why elasticity changes startup cost and capacity planning. Its obstacle list became a research agenda for cloud systems.

#### Key Formulas or Algorithms

Elasticity compares the cost of $n$ servers for one hour with one server for $n$ hours, but demand uncertainty changes the decision. The paper's cost argument weighs overprovisioning loss against underprovisioning loss and cloud rental price.

#### Intuition

Instead of buying servers for a peak that may not occur, a customer requests virtual capacity when demand rises and releases it when demand falls, paying for use. The resulting economics reduce idle capital, but the application still needs plans for provider outages, costly data transfers, variable performance, and lock-in, so elasticity changes capacity planning rather than eliminating operational risk.

#### Main Takeaway

Cloud value comes from elasticity and economies of scale, but realizing it requires solving technical and economic constraints beyond virtualization.

### 60. SkyPilot: An Intercloud Broker for Sky Computing

**Year:** 2023 | **Collection:** 70_plus_dist | [Source](https://www.usenix.org/system/files/nsdi23-yang-zongheng.pdf) | [Local paper](70_plus_dist/023-skypilot-an-intercloud-broker-for-sky-computing-2023.pdf)

#### Research Snapshot

SkyPilot is an intercloud broker that lets a workload describe required resources and then selects, provisions, and recovers feasible cloud instances. It offers portability and price or availability flexibility without requiring providers to standardize their infrastructure.

#### Core Ideas

SkyPilot is an intercloud broker that presents incompatible clouds as a market for compute. Users specify workload requirements, and the broker discovers feasible offerings, provisions resources, manages data and recovery, and can move work across providers.

#### Why It Matters and Impact

Regulation, outages, capacity shortages, and price variation make one-cloud deployment restrictive. SkyPilot demonstrates portability through a broker rather than requiring providers to adopt a uniform infrastructure standard.

#### Key Formulas or Algorithms

For feasible cloud-resource pairs $r$, choose $r^*=\arg\min_r\{\text{price}(r)+\text{transfer}(r)+\text{risk}(r)\}$ subject to accelerator, region, and availability requirements. The controller retries or relaunches on another provider after interruption.

#### Intuition

A user specifies a workload's accelerator, region, storage, price, and recovery requirements once; SkyPilot searches provider-specific offerings, chooses a feasible launch plan, provisions machines, and manages data and job state. If price, capacity, or an interruption invalidates that plan, it retries or relaunches on another compatible cloud, trading portability and resilience against data-transfer and provider-specific capability constraints.

#### Main Takeaway

An intercloud abstraction can provide cloud portability and cost resilience without waiting for full provider standardization.

### 61. Aegean: Replication Beyond the Client-Server Model

**Year:** 2019 | **Collection:** 70_plus_dist | [Source](https://web.eecs.umich.edu/~manosk/assets/papers/aegean-sosp19.pdf) | [Local paper](70_plus_dist/024-aegean-replication-beyond-the-client-server-model-2019.pdf)

#### Research Snapshot

Aegean extends replication protocols to systems in which replicated services call other replicated services. It tracks invocation identities and dependencies so cross-service retries and replication do not duplicate effects or violate execution order.

#### Core Ideas

Aegean extends replication to interacting services by making cross-service calls part of replicated execution, with deterministic request identifiers and dependency tracking.

#### Why It Matters and Impact

Traditional primary-backup and Paxos assume passive clients; service-to-service calls otherwise create duplicated effects or blocking. Aegean preserves correctness while increasing throughput.

#### Key Formulas or Algorithms

Track an invocation dependency graph; execute each request once per replica and release a dependent operation only after its causal predecessor is stable. Deduplicate by $(\mathrm{caller},\mathrm{request\ id})$.

#### Intuition

When a replica executing request $r$ invokes another replicated service, Aegean gives that nested invocation a deterministic identity and records its causal dependency on $r$. Receiving replicas deduplicate retries with that identity and delay dependent execution until the predecessor is stable, so failover cannot turn one logical cross-service call into two effects or expose outcomes in an order replicas disagree about.

#### Main Takeaway

Replication protocols must model service interactions, not only client requests.

### 62. On the Scale and Performance of Cooperative Web Proxy Caching

**Year:** 1999 | **Collection:** 70_plus_dist | [Source](http://www.cs.washington.edu/research/networking/websys/pubs/sosp99/sosp99.pdf) | [Local paper](70_plus_dist/025-on-the-scale-and-performance-of-cooperative-web-proxy-caching-1999.pdf)

#### Research Snapshot

Using proxy traces and analytic modeling, this paper evaluates cooperative Web caching from campus to regional scale. It finds that cache sharing helps only within bounded populations and request-overlap conditions, because coordination costs eventually exceed extra hits.

#### Core Ideas

The study combines proxy traces and an analytic model to determine when cooperative web caches help and when coordination overhead outweighs additional hits.

#### Why It Matters and Impact

It challenged the assumption that more cooperating proxies always improve caching, showing benefits are bounded by population and request overlap.

#### Key Formulas or Algorithms

Compare cooperative hit benefit $\Delta H$ against lookup, bandwidth, and replacement costs; scale the trace model from campus populations to regional populations.

#### Intuition

On a local miss, a proxy can ask peer caches before fetching from the origin, so sharing helps only when different populations request enough of the same objects for extra hits to repay lookup and transfer cost. As the cooperative group grows, request overlap saturates while directory, latency, and replacement overhead grow, making bounded groups or hierarchy better than assuming every cache should cooperate globally.

#### Main Takeaway

Cooperative caching is workload- and scale-dependent, not universally beneficial.

### 63. HALP: Heuristic Aided Learned Preference Eviction Policy for YouTube Content Delivery Network

**Year:** 2023 | **Collection:** 70_plus_dist | [Source](https://www.usenix.org/system/files/nsdi23-song-zhenyu.pdf) | [Local paper](70_plus_dist/026-halp-heuristic-aided-learned-preference-eviction-policy-for-youtube-content-2023.pdf)

#### Research Snapshot

HALP combines a cheap heuristic eviction policy with a learned preference signal for YouTube CDN DRAM caches. It optimizes byte miss ratio under limited CPU overhead and uses impact-distribution analysis to isolate online effects amid production noise.

#### Core Ideas

HALP augments a low-overhead heuristic CDN eviction policy with a learned preference signal and evaluates deployment using impact-distribution analysis.

#### Why It Matters and Impact

The design achieved a production DRAM byte-miss reduction while addressing CPU cost and noisy online measurements that prevent many learned cache policies from shipping.

#### Key Formulas or Algorithms

Rank eviction candidates with a heuristic score corrected by a learned preference; optimize byte miss ratio $\sum 	ext{missed bytes}/\sum 	ext{requested bytes}$ rather than object misses.

#### Intuition

When DRAM is full, HALP uses a low-cost heuristic to identify plausible eviction victims and evaluates only that small set with a learned preference model trained from production access patterns. It evicts the item whose removal is least likely to increase future missed bytes, preserving a CPU budget suitable for every request while optimizing byte miss ratio rather than treating a tiny object and a large video chunk equally.

#### Main Takeaway

Production learned caching works when learning is constrained by efficient heuristics and measured against byte-level impact.

### 64. Antipode: Enforcing Cross-Service Causal Consistency in Distributed Applications

**Year:** 2023 | **Collection:** 70_plus_dist | [Source](https://www.dpss.inesc-id.pt/~rodrigo/antipode-full.pdf) | [Local paper](70_plus_dist/027-antipode-enforcing-cross-service-causal-consistency-in-distributed-applications-2023.pdf)

#### Research Snapshot

Antipode enforces causal consistency across independent services and datastores by carrying operation lineage with user requests and within datastore operations. The incrementally deployable library delays visibility when required causal predecessors are absent.

#### Core Ideas

Antipode propagates operation lineage alongside requests and inside datastores to enforce cross-service causal consistency without a global schema.

#### Why It Matters and Impact

Microservices can expose effects out of causal order across independent stores. Antipode prevents these anomalies with under two percent latency and throughput impact.

#### Key Formulas or Algorithms

If operation $a\rightarrow b$, a read exposing $b$ must expose $a$; attach lineage metadata, merge it through calls, and delay visibility until dependencies are satisfied.

#### Intuition

As a user request crosses services, Antipode attaches lineage describing writes and reads that causally precede its current operation; each service merges and propagates that metadata. Before a datastore exposes a write or read result with dependency $b$, it waits until required predecessors are visible too, preventing a user from observing an effect whose cause is still absent while allowing unrelated operations to proceed.

#### Main Takeaway

End-to-end causal metadata can bolt consistency across otherwise independent datastores.

### 65. NCC: Natural Concurrency Control for Strictly Serializable Datastores by Avoiding the Timestamp-Inversion Pitfall

**Year:** 2023 | **Collection:** 70_plus_dist | [Source](https://www.usenix.org/system/files/osdi23-lu.pdf) | [Local paper](70_plus_dist/028-ncc-natural-concurrency-control-for-strictly-serializable-datastores-by-avoiding-2023.pdf)

#### Research Snapshot

NCC exploits transactions that arrive in an order already compatible with strict serializability. It executes them without locks in one round, verifies consistency with timestamps, and controls response timing to avoid timestamp inversions that could violate real-time order.

#### Core Ideas

NCC executes naturally ordered transactions lock-free in one round, then validates strict serializability with timestamps and controlled response timing.

#### Why It Matters and Impact

Many transactions already arrive in a serializable order, so pessimistic coordination is wasteful. NCC exposes timestamp inversion, where a late response can violate real-time order.

#### Key Formulas or Algorithms

Execute optimistically; validate that serialization timestamps respect conflicts and response order. Use asynchrony-aware timestamps and smart retry to reduce false aborts.

#### Intuition

NCC executes a transaction immediately when its observed conflict order already suggests a valid serialization order, records timestamps and validation evidence, then decides whether it can reply without violating real-time order. If an overlapping transaction's timestamp would invert the order implied by responses, NCC delays or retries the problematic path; the fast path avoids locks and extra rounds, while response control preserves strict serializability.

#### Main Takeaway

Fast strict serializability is possible by exploiting natural order while preventing timestamp inversions.

### 66. Blueprint: A Toolchain for Highly-Reconfigurable Microservice Applications

**Year:** 2023 | **Collection:** 70_plus_dist | [Source](https://people.mpi-sws.org/~dg/papers/sosp23-blueprint.pdf) | [Local paper](70_plus_dist/029-blueprint-a-toolchain-for-highly-reconfigurable-microservice-applications-2023.pdf)

#### Research Snapshot

Blueprint lets developers declare alternative microservice design choices and generates runnable Configure-Build-Deploy variants. It makes component, library, mechanism, and deployment experiments reproducible with little application code rewriting.

#### Core Ideas

Blueprint generates runnable microservice variants from concise design choices, separating configurable architecture dimensions from benchmark application logic.

#### Why It Matters and Impact

It makes experiments with components, libraries, deployment choices, bugs, and fixes reproducible with far less hand-edited code.

#### Key Formulas or Algorithms

A configuration selects implementations for design dimensions; the toolchain composes adapters, builds the variant, and deploys it. The CBD loop is Configure, Build, Deploy.

#### Intuition

Developers describe an application's variable architectural choices, such as a datastore, communication library, protocol, or deployment layout, separately from its stable business logic. Selecting a configuration causes Blueprint to compose adapters and implementations, build the resulting application, and deploy it, so experiments change one explicit dimension at a time and comparisons do not accidentally include hand-edit differences.

#### Main Takeaway

Microservice research is faster and more credible when design changes become declarative and reproducible.

### 67. ServiceRouter: Hyperscale and Minimal Cost Service Mesh at Meta

**Year:** 2023 | **Collection:** 70_plus_dist | [Source](https://www.usenix.org/system/files/osdi23-saokar.pdf) | [Local paper](70_plus_dist/030-servicerouter-hyperscale-and-minimal-cost-service-mesh-at-meta-2023.pdf)

#### Research Snapshot

ServiceRouter is Meta’s service mesh for tens of thousands of services. Most calls use a routing library linked into the client process, avoiding a proxy hop, while routers handle exceptional paths; routing also understands sharded services and geographic locality.

#### Core Ideas

ServiceRouter combines a linked client routing library for most RPCs with proxies where needed, adds sharded-service support, and uses locality rings across regions.

#### Why It Matters and Impact

Avoiding a proxy hop for 99 percent of traffic saves hundreds of thousands of machines at Meta's scale while preserving service-mesh capabilities.

#### Key Formulas or Algorithms

Select endpoints by shard and locality ring, expanding outward on overload or failure; route directly when policy permits, otherwise through an L7 router.

#### Intuition

For an ordinary RPC, a client-linked library consults service discovery, shard ownership, health, and locality rings, then sends directly to the selected backend without an extra sidecar hop. It expands the search to farther or exceptional routing paths on overload or failure, and uses routers where policy requires them; direct routing saves fleet-wide proxy cost while the shared control plane preserves consistent policy.

#### Main Takeaway

Hyperscale service meshes need direct in-process routing, not a proxy on every request.

### 68. AQUATOPE: QoS-and-Uncertainty-Aware Resource Management for Multi-Stage Serverless Workflows

**Year:** 2023 | **Collection:** 70_plus_dist | [Source](https://dl.acm.org/doi/pdf/10.1145/3567955.3567960) | [Local paper](70_plus_dist/031-aquatope-qos-and-uncertainty-aware-resource-management-for-multi-stage-serverless-2023.pdf)

#### Research Snapshot

Aquatope manages multi-stage serverless workflows using Bayesian models of stage performance and uncertainty. It prewarms containers and chooses per-function resource allocations to meet an end-to-end QoS target at minimum expected cost.

#### Core Ideas

Aquatope uses Bayesian performance models to prewarm functions and allocate per-stage resources for multi-stage serverless workflows under uncertain demand.

#### Why It Matters and Impact

End-to-end QoS depends on interacting compute and I/O stages, so independent function tuning wastes resources or causes deadline violations.

#### Key Formulas or Algorithms

Minimize expected cost subject to $P(T_{\mathrm{workflow}}\le D)\ge\eta$; update posterior stage models and choose container warm pools and allocations accordingly.

#### Intuition

For a workflow request, Aquatope combines Bayesian models of each function's runtime, queueing, cold-start risk, and uncertainty to estimate the end-to-end completion distribution. It chooses per-stage memory or CPU allocations and warm-container pools so the probability of meeting the workflow deadline reaches its target at lowest expected cost; uncertainty requires reserves where independent per-function tuning would underestimate tail risk.

#### Main Takeaway

Workflow-aware Bayesian control can reduce serverless cost while making end-to-end latency predictable.

### 69. Doing More with Less: Orchestrating Serverless Applications Without an Orchestrator

**Year:** 2023 | **Collection:** 70_plus_dist | [Source](https://www.usenix.org/system/files/nsdi23-liu-david.pdf) | [Local paper](70_plus_dist/032-doing-more-with-less-orchestrating-serverless-applications-without-an-orchestrator-2023.pdf)

#### Research Snapshot

Unum compiles high-level serverless workflows into function-local orchestration code. Function wrappers use strongly consistent storage to durably claim transitions and coordinate retries, providing decentralized workflow execution without a dedicated orchestrator.

#### Core Ideas

Unum compiles a serverless workflow into decentralized function fragments and an in-situ runtime that coordinates through strongly consistent storage.

#### Why It Matters and Impact

It removes the dedicated orchestrator's cost and rigidity while retaining high-level workflows and exactly-once execution guarantees.

#### Key Formulas or Algorithms

Compile states and transitions into function wrappers; atomically record completion and next-state claims in a consistent store so retries observe the same durable decision.

#### Intuition

The workflow compiler embeds the relevant successor logic in each function wrapper, and wrappers use a strongly consistent store to atomically record a completed state and claim the next transition. When a function retries after a crash or timeout, it reads that durable decision and either resumes the owned transition or observes that another attempt already advanced it, giving workflow-level exactly-once effects without a continuously running orchestrator.

#### Main Takeaway

Application-level orchestration can provide correct workflows using basic serverless primitives.

### 70. Cilantro: Performance-Aware Resource Allocation for General Objectives via Online Feedback

**Year:** 2023 | **Collection:** 70_plus_dist | [Source](https://www.usenix.org/system/files/osdi23-bhardwaj.pdf) | [Local paper](70_plus_dist/033-cilantro-performance-aware-resource-allocation-for-general-objectives-via-online-2023.pdf)

#### Research Snapshot

Cilantro learns each job’s live resource-to-performance relationship and workload changes from online feedback. Confidence-aware allocation policies then optimize a user-selected objective using actual performance metrics instead of static requests or CPU utilization.

#### Core Ideas

Cilantro learns live resource-to-performance mappings and applies confidence-aware policies to optimize user-specified cluster objectives.

#### Why It Matters and Impact

CPU utilization is not user experience. Directly observing metrics such as P95 latency supports different fairness and utility goals without offline profiling.

#### Key Formulas or Algorithms

Learn $f_i(x_i,\ell_i)$ from online feedback, then optimize $\max_x\sum_i U_i(f_i(x_i))$ with $\sum_i x_i\le C$, using confidence bounds for uncertain estimates.

#### Intuition

After each resource allocation, Cilantro observes each job's user metric, load, and response to allocated CPU or other resources, and updates a confidence-aware performance model. It then reallocates a fixed cluster budget to optimize the chosen utility or fairness objective, exploring uncertain choices cautiously; the tradeoff is temporary learning exploration for decisions based on actual latency or throughput instead of misleading utilization.

#### Main Takeaway

Online performance feedback makes resource allocation adaptive to changing jobs and objectives.

### 71. Autothrottle: A Practical Bi-Level Approach to Resource Management for SLO-Targeted Microservices

**Year:** 2024 | **Collection:** 70_plus_dist | [Source](https://arxiv.org/pdf/2212.12180) | [Local paper](70_plus_dist/034-autothrottle-a-practical-bi-level-approach-to-resource-management-for-slo-2024.pdf)

#### Research Snapshot

Autothrottle uses two control levels for latency-SLO microservices: a global learning controller assigns per-service CPU-throttle targets, and local controllers enforce them. This links end-to-end latency feedback to resource decisions without centralizing every adjustment.

#### Core Ideas

Autothrottle separates a global learning controller that sets CPU-throttle targets from local per-service controllers that enforce them.

#### Why It Matters and Impact

Microservice end-to-end SLOs cannot be controlled reliably through isolated service utilization. The two-level design saves CPU while protecting latency.

#### Key Formulas or Algorithms

The upper controller chooses throttle vector $	au$ to minimize CPU subject to $P99(	au)\le\mathrm{SLO}$; lower controllers adjust local quotas toward their assigned targets.

#### Intuition

The upper controller observes end-to-end latency and chooses a vector of CPU throttle targets for services, balancing saved CPU against the SLO; each service's local controller rapidly adjusts its own quota toward that target. The separation lets local loops handle enforcement without central delay, while the global loop accounts for cross-service latency dependencies that isolated utilization-based controllers cannot see.

#### Main Takeaway

Bridging end-to-end feedback and per-service control enables SLO-aware CPU efficiency.

### 72. The Byzantine Generals Problem

**Year:** 1982 | **Collection:** 70_plus_dist | [Source](https://lamport.azurewebsites.net/pubs/byz.pdf) | [Local paper](70_plus_dist/035-the-byzantine-generals-problem-1982.pdf)

#### Research Snapshot

The Byzantine Generals Problem formalizes agreement when some participants can send arbitrary, inconsistent messages. It proves that unauthenticated oral-message agreement requires more than two-thirds loyal participants and shows how signatures change the resilience conditions.

#### Core Ideas

The paper formalizes agreement among generals when some send arbitrary, conflicting messages, distinguishing oral from signed messages.

#### Why It Matters and Impact

It established the Byzantine fault model and the fundamental resilience threshold behind replicated services and blockchains.

#### Key Formulas or Algorithms

With oral messages, agreement requires $n>3f$; algorithm $OM(m)$ recursively relays commanders' values for $m$ rounds and decides by majority. Signatures prevent forgery and permit tolerance of any number of traitors short of all participants.

#### Intuition

The commander sends an order and recipients relay what they received for a bounded number of rounds, then each loyal general applies the same majority rule to the collected message tree. Byzantine generals may omit, forge context, or tell different recipients different values, but with oral messages $n>3f$ gives loyal quorums enough overlap to agree; signed messages prevent a traitor from inventing another general's order and change the resilience tradeoff.

#### Main Takeaway

Byzantine agreement needs more than two-thirds loyal participants unless messages are unforgeable.

### 73. The Weak Byzantine Generals Problem

**Year:** 1983 | **Collection:** 70_plus_dist | [Source](https://lamport.azurewebsites.net/pubs/weak-byz.pdf) | [Local paper](70_plus_dist/036-the-weak-byzantine-generals-problem-1983.pdf)

#### Research Snapshot

The weak Byzantine agreement problem permits a common outcome that may be invalid after a failure, modeling cases such as transaction commit. Exact solutions still require fewer than one-third Byzantine failures, while approximation can tolerate more failures by weakening the outcome guarantee.

#### Core Ideas

Weak Byzantine agreement permits a common default or incorrect value after failures, capturing problems such as distributed transaction commit.

#### Why It Matters and Impact

Relaxing validity does not remove the one-third bound for exact agreement, but it enables approximate solutions that tolerate arbitrarily many failures.

#### Key Formulas or Algorithms

The weak condition preserves agreement among nonfaulty processes while validity applies only in fault-free executions; exact solutions still need $n>3f$.

#### Intuition

Processes must still terminate with one common result, but unlike full Byzantine agreement the result may be a distinguished default such as abort after a fault rather than a commander's original value. This weaker validity matches transaction commit, yet indistinguishable conflicting messages still impose the $n>3f$ bound for exact solutions; only further approximation of the result can tolerate more Byzantine participants.

#### Main Takeaway

Relaxing what counts as a valid outcome can make fault-tolerant agreement more achievable.

### 74. An Overview of Blockchain Technology: Architecture, Consensus, and Future Trends

**Year:** 2017 | **Collection:** 70_plus_dist | [Source](http://inpluslab.com/files/2-An%20Overview%20of%20Blockchain%20Technology%20Architecture,%20Consensus,%20and%20Future%20Trends.pdf) | [Local paper](70_plus_dist/037-an-overview-of-blockchain-technology-architecture-consensus-and-future-trends-2017.pdf)

#### Research Snapshot

This survey explains blockchain architecture, including replicated ledgers, peer-to-peer dissemination, cryptographic linking, consensus, and smart contracts. It compares consensus approaches and identifies security, privacy, and scalability limitations.

#### Core Ideas

The survey decomposes blockchain into distributed ledger, cryptography, peer-to-peer networking, consensus, smart contracts, and application layers.

#### Why It Matters and Impact

It maps the design space and highlights scalability, privacy, and security challenges beyond Bitcoin's original payment use case.

#### Key Formulas or Algorithms

A block links through $h_i=H(\mathrm{header}_i)$ containing the previous hash; consensus selects one valid chain, commonly by proof-of-work or stake-weighted voting.

#### Intuition

Peers disseminate signed transactions, assemble candidate blocks containing the previous block's hash, and run a consensus rule such as proof of work or stake-weighted voting to select one history. Every replica validates links and transactions before extending its local ledger, so rewriting an earlier block requires overcoming later cryptographic and consensus evidence; the survey's key tradeoff is decentralized trust against throughput, latency, privacy, and energy cost.

#### Main Takeaway

Blockchain combines replicated logs and cryptography, but its consensus and scalability trade-offs remain central.

### 75. Flexible Advancement in Asynchronous BFT Consensus

**Year:** 2023 | **Collection:** 70_plus_dist | [Source](https://dl.acm.org/doi/pdf/10.1145/3600006.3613164) | [Local paper](70_plus_dist/038-flexible-advancement-in-asynchronous-bft-consensus-2023.pdf)

#### Research Snapshot

The paper separates block ordering from agreement in asynchronous Byzantine consensus. Its SuperMA multi-valued agreement protocol and MyTumbler replication design permit flexible proposal and commitment behavior while maintaining Byzantine safety.

#### Core Ideas

The work separates ordering from agreement in asynchronous BFT and introduces SuperMA, a three-message-delay multi-valued agreement core used by MyTumbler.

#### Why It Matters and Impact

Flexible block proposal and commitment adapt better to WAN workloads than fixed single-leader designs while preserving Byzantine safety.

#### Key Formulas or Algorithms

SuperMA collects sufficient certified proposals and terminates in three message delays in the best case; MyTumbler orders blocks with timestamp evidence and invokes agreement for conflicts.

#### Intuition

Replicas can disseminate and order candidate blocks independently, then invoke SuperMA only when they need a Byzantine-safe common advancement decision. The agreement phase collects certified proposals and enough matching evidence that correct replicas select compatible outcomes despite arbitrary faulty messages; separating these roles lets the fast ordering pipeline move flexibly while agreement preserves safety under asynchronous delivery.

#### Main Takeaway

Decoupling ordering and agreement gives asynchronous BFT protocols flexibility without abandoning efficient commitment.

### 76. uBFT: Microsecond-Scale BFT Using Disaggregated Memory

**Year:** 2022 | **Collection:** 70_plus_dist | [Source](https://arxiv.org/pdf/2210.17174) | [Local paper](70_plus_dist/039-ubft-microsecond-scale-bft-using-disaggregated-memory-2022.pdf)

#### Research Snapshot

uBFT uses RDMA-accessible disaggregated memory as a small trusted component for Byzantine state-machine replication. Its Consistent Tail Broadcast abstraction prevents equivocation over a bounded recent message history, enabling low latency with $2f+1$ replicas.

#### Core Ideas

uBFT uses RDMA-accessible disaggregated memory as a small trusted base and Consistent Tail Broadcast to prevent equivocation with bounded memory.

#### Why It Matters and Impact

It reaches roughly 10-microsecond BFT replication latency with $2f+1$ replicas, far faster than enclave-based alternatives.

#### Key Formulas or Algorithms

Consistent Tail Broadcast stores a non-equivocating recent message tail; with trusted shared memory, $2f+1$ replicas tolerate $f$ Byzantine faults instead of the usual $3f+1$.

#### Intuition

Replicas use RDMA to append recent protocol messages to a bounded trusted-memory tail that every reader sees consistently, so a Byzantine sender cannot equivocate by presenting different tails to different replicas. Protocol steps read that shared evidence before advancing, allowing $2f+1$ replicas to tolerate $f$ faults and commit with microsecond latency; the benefit depends on trusting the disaggregated-memory component rather than assuming only Byzantine software replicas.

#### Main Takeaway

Trusted disaggregated memory can trade a small hardware assumption for microsecond-scale BFT.

### 77. Impossibility of Distributed Consensus with One Faulty Process

**Year:** 1983 | **Collection:** 70_plus_dist | [Source](https://groups.csail.mit.edu/tds/papers/Lynch/jacm85.pdf) | [Local paper](70_plus_dist/040-impossibility-of-distributed-consensus-with-one-faulty-process-1983.pdf)

#### Research Snapshot

FLP proves that no deterministic protocol can guarantee consensus termination in a fully asynchronous message-passing system with even one possible crash. An adversarial message schedule can preserve a state from which either decision remains possible forever.

#### Core Ideas

FLP proves that deterministic consensus in a fully asynchronous message-passing system can be kept from terminating by one crash failure.

#### Why It Matters and Impact

The result explains why practical consensus protocols need timing assumptions, randomization, or failure detectors for liveness.

#### Key Formulas or Algorithms

A configuration is bivalent if both decisions remain reachable. From any bivalent state, an adversarial scheduler can choose a message delivery that preserves bivalence indefinitely.

#### Intuition

From a bivalent configuration, where either decision remains possible, an adversarial scheduler delivers one carefully chosen enabled message that leaves the configuration bivalent again and can postpone another process forever as the one allowed crash. Because a correct process cannot distinguish that schedule from arbitrary network slowness, any deterministic protocol must either wait forever or risk disagreeing; the theorem leaves safety possible but rules out guaranteed termination without extra assumptions.

#### Main Takeaway

Safety alone is insufficient: deterministic asynchronous consensus cannot guarantee termination with even one crash.

### 78. The Part-Time Parliament

**Year:** 1998 | **Collection:** 70_plus_dist | [Source](https://lamport.azurewebsites.net/pubs/lamport-paxos.pdf) | [Local paper](70_plus_dist/041-the-part-time-parliament-1998.pdf)

#### Research Snapshot

The Part-Time Parliament derives Paxos as a protocol for maintaining a replicated log despite lost messages and intermittently available participants. Ballots and intersecting majorities ensure later proposals preserve any value already chosen.

#### Core Ideas

The Part-Time Parliament presents Paxos as a legislature that maintains a replicated sequence despite absent legislators and lost messages.

#### Why It Matters and Impact

It gave the state-machine replication problem a rigorous quorum-based solution and the conceptual foundation for Paxos deployments.

#### Key Formulas or Algorithms

A ballot chooses value $v$ only after a majority accepts it. A proposer with ballot $b$ adopts the value of the highest prior accepted ballot returned by a majority, preserving quorum intersection.

#### Intuition

For a log slot, a proposer first obtains promises from a majority not to accept lower-numbered ballots and learns any values those acceptors already accepted. It then proposes the value from the highest prior ballot, or a new value only if none exists, and a majority accepts it; because any two majorities intersect, a later ballot cannot replace an already chosen decree even when legislators are absent and messages are lost.

#### Main Takeaway

Quorum intersection and ballot promises preserve one ordered history despite unreliable participants.

### 79. Paxos Made Simple

**Year:** 2001 | **Collection:** 70_plus_dist | [Source](https://lamport.azurewebsites.net/pubs/paxos-simple.pdf) | [Local paper](70_plus_dist/042-paxos-made-simple-2001.pdf)

#### Research Snapshot

Paxos Made Simple presents single-decree Paxos using numbered proposals, proposers, acceptors, and learners. A proposer first learns prior acceptances from a quorum, then carries forward the highest-numbered accepted value before asking that quorum to accept.

#### Core Ideas

Paxos Made Simple states the single-decree protocol with proposers, acceptors, learners, and numbered proposals.

#### Why It Matters and Impact

Its concise presentation made the safety invariant accessible: once chosen, a value cannot be replaced by another.

#### Key Formulas or Algorithms

Phase 1: send prepare($n$), acceptors promise not to accept lower numbers and return accepted pairs. Phase 2: propose the returned highest-numbered value, then accept($n,v$); a majority chooses $v$.

#### Intuition

An initiator chooses a unique proposal number, sends `prepare`, and waits for promises from a majority; each acceptor refuses lower numbers and reports its highest accepted pair. The initiator must carry forward the value of the highest reported pair in `accept`, then learners treat the value as chosen only after a majority accepts it, preserving one decision despite competing proposers and message reordering.

#### Main Takeaway

A proposer may choose freely only when its quorum reports no earlier accepted value.

### 80. Mencius: Building Efficient Replicated State Machines for WANs

**Year:** 2008 | **Collection:** 70_plus_dist | [Source](https://www.usenix.org/legacy/events/osdi08/tech/full_papers/mao/mao.pdf) | [Local paper](70_plus_dist/043-mencius-building-efficient-replicated-state-machines-for-wans-2008.pdf)

#### Research Snapshot

Mencius distributes Paxos leadership by assigning each replica a fixed sequence of log slots. Clients can use nearby owners, while no-op proposals let replicas bypass slots whose owner is idle or slow without breaking the common order.

#### Core Ideas

Mencius assigns each replica a rotating set of consensus slots, letting clients use nearby leaders while allowing others to skip idle slots.

#### Why It Matters and Impact

The multi-leader Paxos derivative improves WAN latency under low load and throughput under high load without a permanent bottleneck.

#### Key Formulas or Algorithms

Replica $i$ owns slots $i,i+n,i+2n,\ldots$; it fast-proposes its slots, while other replicas issue no-ops to skip stalled owners and preserve global order.

#### Intuition

Replicas deterministically own interleaved log slots, so a client can send a request to a nearby owner and that owner can fast-propose its own slots without competing for a global leader. Replicas execute slots only in sequence; when an owner's earlier slot blocks progress, another replica proposes a no-op for it, trading an occasional empty entry for liveness while quorum agreement retains one common state-machine order.

#### Main Takeaway

Static slot ownership distributes leadership while no-op skipping maintains ordered progress.

### 81. Bitcoin-NG: A Scalable Blockchain Protocol

**Year:** 2016 | **Collection:** 70_plus_dist | [Source](https://www.usenix.org/system/files/conference/nsdi16/nsdi16-paper-eyal.pdf) | [Local paper](70_plus_dist/044-bitcoin-ng-a-scalable-blockchain-protocol-2016.pdf)

#### Research Snapshot

Bitcoin-NG separates proof-of-work leader election from transaction serialization. A mined key block elects a temporary leader, which issues frequent signed microblocks until the next key block, improving throughput without shortening the mining interval.

#### Core Ideas

Bitcoin-NG separates infrequent proof-of-work key blocks from frequent signed microblocks produced by the elected leader.

#### Why It Matters and Impact

This decouples leader election from transaction serialization, increasing throughput without increasing fork rate or weakening Bitcoin's trust model.

#### Key Formulas or Algorithms

Miners race for key blocks; the winner's key signs a microblock chain. Security metrics include consensus delay and fairness, while throughput is bounded by node bandwidth rather than block interval.

#### Intuition

A proof-of-work key block elects one leader and commits the leader's public key; until the next key block appears, that leader serializes transactions into frequent signed microblocks. Nodes verify the signature chain and resolve competing key-block branches by the underlying mining rule, so transaction throughput can rise toward bandwidth limits without shortening the leader-election interval and increasing fork risk.

#### Main Takeaway

Separating mining from transaction processing removes Bitcoin's block-size and interval bottleneck.

### 82. Beehive: O(1) Lookup Performance for Power-Law Query Distributions in Peer-to-Peer Overlays

**Year:** 2004 | **Collection:** 70_plus_dist | [Source](https://www.usenix.org/legacy/publications/library/proceedings/nsdi04/tech/full_papers/ramasubramanian/ramasubramanian.pdf) | [Local paper](70_plus_dist/045-beehive-o-1-lookup-performance-for-power-law-query-distributions-in-peer-to-peer-2004.pdf)

#### Research Snapshot

Beehive proactively replicates DHT objects according to a power-law request distribution. A closed-form allocation gives popular objects enough replicas for constant expected lookup cost while retaining the DHT for rare objects and adapting to popularity shifts.

#### Core Ideas

Beehive proactively replicates objects in a DHT according to Zipf-like query popularity, using a closed-form replication allocation.

#### Why It Matters and Impact

It reduces average overlay lookup from $O(\log N)$ to $O(1)$ for common power-law workloads with modest storage and adaptation overhead.

#### Key Formulas or Algorithms

For popularity $p_i$, choose replica level $r_i$ so popular objects occupy exponentially more nodes; route locally when replicated, otherwise use the base DHT lookup.

#### Intuition

Beehive estimates each key's Zipf-like request rate and creates more replicas for popular keys at carefully chosen overlay locations, while rare keys keep only their base DHT placement. A lookup first checks the local replica levels and falls back to logarithmic DHT routing if needed; allocating storage by demand makes the expected lookup path constant for the common case without requiring every key to be everywhere.

#### Main Takeaway

Demand-aware proactive replication can make structured overlays fast for the queries people actually issue.

### 83. AnySee: Peer-to-Peer Live Streaming

**Year:** 2004 | **Collection:** 70_plus_dist | [Source](https://ieeexplore.ieee.org/document/4146941) | [Local paper](70_plus_dist/046-anysee-peer-to-peer-live-streaming-2004.pdf)

#### Research Snapshot

AnySee improves peer-to-peer live streaming by allocating peers across multiple overlays rather than optimizing every stream independently. It uses locality, delay, and upload capacity to share unused resources and balance load globally.

#### Core Ideas

AnySee uses inter-overlay optimization: peers may contribute resources across multiple live-stream overlays and are assigned by locality, delay, and load.

#### Why It Matters and Impact

This improves global utilization and playback quality beyond designs that optimize each overlay independently, and was deployed to tens of thousands of users.

#### Key Formulas or Algorithms

Choose supplying peers by minimizing network distance and balancing upload capacity; permit cross-overlay assignments when they improve source-to-end delay or relieve a hot group.

#### Intuition

The system measures peers' upload capacity, delay, and network location across many live-stream overlays, then assigns available peers to supply chunks where they reduce a bottleneck rather than only to the channel they joined. A receiver still needs timely video chunks, but cross-overlay assignments use otherwise idle upload capacity and avoid concentrating load on a single source or locality.

#### Main Takeaway

Cross-overlay resource sharing improves P2P live streaming when the physical network is considered globally.

### 84. Dynamo: Amazon's Highly Available Key-Value Store

**Year:** 2007 | **Collection:** 70_plus_dist | [Source](https://www.allthingsdistributed.com/files/amazon-dynamo-sosp2007.pdf) | [Local paper](70_plus_dist/047-dynamo-amazon-s-highly-available-key-value-store-2007.pdf)

#### Research Snapshot

Dynamo is a highly available key-value store built from consistent-hash partitioning, replicated preference lists, quorum reads and writes, vector clocks, hinted handoff, and anti-entropy. It accepts temporary version divergence during failures and exposes conflicts for application resolution.

#### Core Ideas

Dynamo uses consistent-hash partitioning, preference lists, quorum reads and writes, vector clocks, hinted handoff, and anti-entropy to prioritize availability.

#### Why It Matters and Impact

It showed how an always-on retail service can remain writable through failures by exposing and reconciling divergent object versions.

#### Key Formulas or Algorithms

For replication factor $N$, write quorum $W$ and read quorum $R$ give strong overlap when $R+W>N$; vector clocks identify concurrent versions rather than imposing a false order.

#### Intuition

For each key, Dynamo routes reads and writes to a preference list of $N$ replicas; a client waits for $W$ write or $R$ read responses, while hinted handoff accepts work for an unavailable owner. During a partition, concurrent writers can create incomparable vector clocks rather than silently overwrite each other; later reads return those siblings for reconciliation and anti-entropy spreads the merged result, favoring availability over immediate single-copy consistency.

#### Main Takeaway

High availability often requires explicit versioning and application-assisted conflict resolution.

### 85. Revisiting Log-Structured Merging for KV Stores in Hybrid Memory Systems

**Year:** 2023 | **Collection:** 70_plus_dist | [Source](https://dl.acm.org/doi/pdf/10.1145/3575693.3575715) | [Local paper](70_plus_dist/048-revisiting-log-structured-merging-for-kv-stores-in-hybrid-memory-systems-2023.pdf)

#### Research Snapshot

MioDB redesigns LSM-based storage for byte-addressable nonvolatile memory. Persistent skip lists, one-piece flushing, elastic buffers, zero-copy compaction, and parallel scheduling reduce serialization, write stalls, write amplification, and tail latency.

#### Core Ideas

MioDB redesigns LSM merging for byte-addressable NVM using persistent skip lists, one-piece flushing, elastic buffers, zero-copy and parallel compaction.

#### Why It Matters and Impact

It addresses serialization cost and flush-compaction imbalance that cause write stalls and tail latency in hybrid-memory KV stores.

#### Key Formulas or Algorithms

LSM write amplification is $WA=	ext{bytes written}/	ext{user bytes}$; MioDB moves runs without serialization and overlaps flushing with multi-level compaction to lower $WA$ and stalls.

#### Intuition

Writes first enter persistent-memory structures that can be searched and moved without repeatedly serializing records into temporary disk formats. When buffers fill, MioDB flushes pieces and schedules zero-copy, parallel compaction across levels so a large merge does not block incoming writes; the design trades more specialized NVM-aware metadata for lower write amplification and fewer tail-latency stalls.

#### Main Takeaway

NVM-aware layouts and compaction scheduling make LSM stores faster and more predictable.

### 86. SILT: A Memory-Efficient, High-Performance Key-Value Store

**Year:** 2008 | **Collection:** 70_plus_dist | [Source](http://sigops.org/sosp/sosp11/current/2011-Cascais/printable/01-lim.pdf) | [Local paper](70_plus_dist/049-silt-a-memory-efficient-high-performance-key-value-store-2008.pdf)

#### Research Snapshot

SILT combines several flash-backed key-value store layouts to balance memory use, writes, and lookups. Compact RAM indexes direct a request to nearly one flash location, allowing billions of items with very little DRAM per key.

#### Core Ideas

SILT composes three flash-backed KV-store designs, including a log store, sorted store, and small-index large-table layout, selected for workload needs.

#### Why It Matters and Impact

It serves billions of items on one machine with about 0.7 DRAM bytes per item and nearly one flash read per lookup.

#### Key Formulas or Algorithms

A compact in-memory index narrows a lookup to a small flash range; cuckoo hashing and entropy-coded keys reduce RAM while sorted immutable tables support efficient reads.

#### Intuition

SILT stores key-value data in flash-oriented components chosen for their update and lookup behavior, while a compact RAM index, fingerprints, and encoded key information narrow a request to a tiny flash range. A lookup checks that compact metadata, issues nearly one flash read, and verifies the key; the invariant is that false candidates are detected, allowing billions of keys with much less DRAM than a full hash table.

#### Main Takeaway

Careful synthesis of indexing and storage layouts can make flash KV stores both memory-frugal and fast.

### 87. Snape: Reliable and Low-Cost Computing with a Mixture of Spot and On-Demand VMs

**Year:** 2023 | **Collection:** 70_plus_dist | [Source](https://dl.acm.org/doi/pdf/10.1145/3582016.3582028) | [Local paper](70_plus_dist/050-snape-reliable-and-low-cost-computing-with-a-mixture-of-spot-and-on-demand-vms-2023.pdf)

#### Research Snapshot

Snape uses observed spot-instance interruption behavior and constrained reinforcement learning to choose a changing mix of cheap preemptible and reliable on-demand VMs. The policy minimizes cost while enforcing an availability target.

#### Core Ideas

Snape predicts spot-VM eviction characteristics and uses constrained reinforcement learning to mix cheap spot capacity with reliable on-demand capacity.

#### Why It Matters and Impact

It turns an opaque cost-availability trade-off into an online policy, achieving substantial savings while maintaining high availability.

#### Key Formulas or Algorithms

Learn a policy maximizing cost savings subject to $A\ge A_{\min}$, where availability $A$ accounts for predicted preemptions; adjust spot fraction after observing interruptions and demand.

#### Intuition

At each decision point Snape observes demand, recent spot interruption patterns, and the currently running fleet, then selects how many cheap preemptible and reliable on-demand VMs to use. Its constrained learning policy changes the mix only when predicted available capacity remains above the service target; it accepts some replacement work and uncertainty to capture spot savings without violating the availability constraint.

#### Main Takeaway

Predictive, constrained control makes spot instances useful for availability-sensitive workloads.

### 88. Bamboo: Making Preemptible Instances Resilient for Affordable Training of Large DNNs

**Year:** 2023 | **Collection:** 70_plus_dist | [Source](https://www.usenix.org/system/files/nsdi23-thorpe.pdf) | [Local paper](70_plus_dist/051-bamboo-making-preemptible-instances-resilient-for-affordable-training-of-large-2023.pdf)

#### Research Snapshot

Bamboo makes pipeline-parallel DNN training resilient to preemptible VM loss by using idle pipeline bubbles for redundant neighbor-stage computation. The extra state lets surviving workers continue or recover work without frequent expensive checkpoints.

#### Core Ideas

Bamboo exploits idle pipeline bubbles to redundantly compute neighboring DNN layers, allowing training to survive frequent preemptible-instance loss.

#### Why It Matters and Impact

Redundancy placed in otherwise idle pipeline time outperforms conventional checkpoint-and-restart for low-cost large-model training.

#### Key Formulas or Algorithms

If stage $i$ has a bubble, compute a backup of neighbor stage $i+1$'s activation or gradient; after failure, the redundant state replaces lost work without remote checkpoint recovery.

#### Intuition

Pipeline parallelism creates predictable idle bubbles while microbatches move between stages; Bamboo uses those bubbles to compute and retain redundant activations or gradients for neighboring stages. When a preemptible VM disappears, survivors use that duplicate state to reconstruct the lost stage and continue the iteration, trading spare bubble computation and memory for avoiding a costly global checkpoint rollback.

#### Main Takeaway

Pipeline slack can be converted into inexpensive resilience for preemptible training.

### 89. TinyDB: An Acquisitional Query Processing System for Sensor Networks

**Year:** 2000 | **Collection:** 70_plus_dist | [Source](https://dsf.berkeley.edu/papers/tods05-tinydb.pdf) | [Local paper](70_plus_dist/052-tinydb-an-acquisitional-query-processing-system-for-sensor-networks-2000.pdf)

#### Research Snapshot

TinyDB introduces acquisitional query processing for sensor networks, where a query optimizer controls when, where, and how often sensors acquire readings. It combines sample scheduling, in-network filtering, aggregation, and communication planning to save energy.

#### Core Ideas

TinyDB introduces acquisitional query processing, where the optimizer controls when, where, and how frequently sensors sample rather than treating readings as free stored data.

#### Why It Matters and Impact

Sensor acquisition and radio transmission dominate energy use, so database-style pushdown alone is insufficient for long-lived sensor networks.

#### Key Formulas or Algorithms

For sampling interval $\delta$, optimize energy $E(\delta)=E_{\mathrm{sample}}/\delta+E_{\mathrm{radio}}(\delta)$ subject to query fidelity. Push predicates and aggregation into the network and schedule shared samples.

#### Intuition

A query specifies predicates, aggregates, and sampling needs, and TinyDB's optimizer chooses when sensors wake, which nodes sample, and where values are filtered or aggregated on the routing tree. Nodes share samples across queries and send compact aggregates instead of raw readings, preserving query fidelity while minimizing the battery cost of sensing and radio communication.

#### Main Takeaway

In sensor systems, acquiring data is a query-planning decision with direct energy cost.

### 90. Take Out the TraChe: Maximizing (Tra)nsactional Ca(che) Hit Rate

**Year:** 2023 | **Collection:** 70_plus_dist | [Source](https://www.usenix.org/system/files/osdi23-cheng.pdf) | [Local paper](70_plus_dist/053-take-out-the-trache-maximizing-tra-nsactional-ca-che-hit-rate-2023.pdf)

#### Research Snapshot

DeToX defines transactional hit rate, measuring whether a cache eliminates storage waits for an entire transaction rather than for one object. It uses transaction dependencies to prefetch jointly needed data and evict objects with low transaction-level value.

#### Core Ideas

DeToX defines transactional hit rate and uses transaction dependencies to choose cache prefetch and eviction decisions rather than optimizing individual object hits.

#### Why It Matters and Impact

A cache hit matters only when it accelerates a whole transaction; object-level policies can retain popular data that never removes transaction stalls.

#### Key Formulas or Algorithms

Transactional hit rate is $\frac{\text{transactions served without storage wait}}{\text{transactions}}$. Build dependency sets, prefetch likely co-accessed objects, and evict objects with low transaction-level value.

#### Intuition

DeToX observes which records a transaction needs together and treats the transaction as a cache hit only when every storage-dependent access can proceed without a miss. It prefetches likely dependency sets and evicts records whose removal least reduces completed transactions, so limited cache space is directed toward eliminating full transaction stalls rather than accumulating unrelated object-level hits.

#### Main Takeaway

Caching should optimize end-to-end transactional completion, not isolated object hits.

### 91. Turbo: Effective Caching in Differentially Private Databases

**Year:** 2023 | **Collection:** 70_plus_dist | [Source](https://arxiv.org/pdf/2306.16163v2) | [Local paper](70_plus_dist/054-turbo-effective-caching-in-differentially-private-databases-2023.pdf)

#### Research Snapshot

Turbo uses PMW-Bypass, a private multiplicative-weights model trained from previously released differentially private query answers. It answers later linear queries from the model when error is acceptable, conserving privacy budget, and obtains new private answers only when needed.

#### Core Ideas

Turbo turns private multiplicative weights into PMW-Bypass, a cache that reuses prior differentially private answers to answer future linear queries without further privacy loss when accurate enough.

#### Why It Matters and Impact

Privacy budget is finite, so effective caching improves both analytics capacity and latency. Turbo conserves substantially more budget than prior approaches.

#### Key Formulas or Algorithms

DP requires $P[M(D)\in S]\le e^\epsilon P[M(D')\in S]+\delta$. PMW maintains a synthetic distribution; answer from it when error is bounded, otherwise obtain a new DP answer and update it.

#### Intuition

The system maintains a synthetic distribution learned from previously released differentially private answers and estimates that model's error for each new linear query. If the error bound is acceptable, it returns the model answer with no new privacy loss; otherwise it spends privacy budget on a fresh noisy answer and updates the model, trading occasional accuracy-driven budget expenditure for many low-latency reused answers.

#### Main Takeaway

A learned DP answer cache can trade model accuracy for much lower privacy-budget consumption.

### 92. XFaaS: Hyperscale and Low-Cost Serverless Functions at Meta

**Year:** 2023 | **Collection:** 70_plus_dist | [Source](https://tangchq74.github.io/XFaaS-SOSP23-Final.pdf) | [Local paper](70_plus_dist/055-xfaas-hyperscale-and-low-cost-serverless-functions-at-meta-2023.pdf)

#### Research Snapshot

XFaaS runs Meta’s serverless platform with broad function availability, global dispatch, deferred execution of delay-tolerant work, and TCP-like downstream congestion control. These mechanisms reduce cold-start and spike-provisioning costs while protecting dependent services.

#### Core Ideas

XFaaS runs Meta's FaaS fleet using broad function availability, deferred execution for delay-tolerant work, global dispatch, and TCP-like downstream congestion control.

#### Why It Matters and Impact

It demonstrates that hyperscale serverless need not imply low utilization: the platform processes trillions of calls daily at high average CPU utilization.

#### Key Formulas or Algorithms

Increase function admission window on success and reduce it on downstream overload, analogous to TCP congestion control; shift flexible calls to off-peak capacity and remote regions.

#### Intuition

The platform makes functions broadly runnable across regions, dispatches urgent calls to available capacity, and defers delay-tolerant calls into slack periods. It also increases downstream request admission after success and cuts it on overload, like TCP congestion control, so a burst neither forces permanent idle provisioned capacity nor cascades into overloaded dependent services.

#### Main Takeaway

High-utilization FaaS requires global scheduling and backpressure, not only fast cold starts.

### 93. Global Capacity Management with Flux

**Year:** 2023 | **Collection:** 70_plus_dist | [Source](https://www.usenix.org/system/files/osdi23-eriksen.pdf) | [Local paper](70_plus_dist/056-global-capacity-management-with-flux-2023.pdf)

#### Research Snapshot

Flux automates regional capacity planning for large dependent service graphs. It derives capacity models from RPC traces, jointly selects traffic and machine distributions across regions, and safely rebalances toward the plan as supply and demand change.

#### Core Ideas

Flux automates regional capacity allocation using RPC traces to infer service dependency and capacity models, then jointly plans traffic and machines across regions.

#### Why It Matters and Impact

Manual regionalization cannot keep pace with thousands of dependent services and changing heterogeneous capacity.

#### Key Formulas or Algorithms

Solve for traffic $x_{sr}$ and capacity $c_{sr}$ minimizing cost subject to demand, dependency, and regional constraints; continuously orchestrate safe rebalancing toward the plan.

#### Intuition

Flux derives a graph of caller-to-callee demand from RPC traces, estimates each service's regional capacity needs, and solves for a joint traffic and machine distribution. It then applies the plan in dependency-aware stages, provisioning or protecting downstream capacity before shifting callers, so global cost or utilization improvements do not cause a transient overload in an unseen dependent service.

#### Main Takeaway

Global capacity planning must model service dependencies and execute rebalancing safely.

### 94. Borg: The Next Generation

**Year:** 2019 | **Collection:** 70_plus_dist | [Source](https://dl.acm.org/doi/pdf/10.1145/3342195.3387517) | [Local paper](70_plus_dist/057-borg-the-next-generation-2019.pdf)

#### Research Snapshot

This trace study compares eight 2019 Borg clusters with the 2011 Borg trace. It documents changes in workload mix, alloc sets, vertical scaling, overcommitment, dependency-related failures, and extremely heavy-tailed resource consumption.

#### Core Ideas

The paper analyzes the 2019 Google Borg traces and compares them to 2011, documenting evolved workload classes, alloc sets, autoscaling, overcommitment, and heavy tails.

#### Why It Matters and Impact

It supplies evidence about how production scheduling changed rather than presenting a new scheduler, informing workload models and benchmark assumptions.

#### Key Formulas or Algorithms

The top one percent of jobs consume over 99 percent of resources; compare arrival, resource, failure, and placement distributions across clusters and years.

#### Intuition

The authors aggregate production traces by job, alloc set, resource request, scaling behavior, failure, and placement, then compare their distributions with earlier Borg traces. Since a tiny fraction of jobs consumes most resources, average-job assumptions hide the state that drives admission and placement decisions; the practical lesson is to model heavy tails and modern workload features before evaluating a scheduler.

#### Main Takeaway

Modern cluster-management research must account for heavy-tailed workloads and evolved production features.

### 95. Characterizing Smart Home IoT Traffic in the Wild

**Year:** 2001 | **Collection:** 70_plus_dist | [Source](https://arxiv.org/pdf/2001.08288) | [Local paper](70_plus_dist/058-characterizing-smart-home-iot-traffic-in-the-wild-2001.pdf)

#### Research Snapshot

This measurement study passively collected smart-home IoT traffic from more than 200 homes. It characterizes device volume, timing, destinations, encryption, and third-party dependencies, finding central reliance on a few cloud and DNS providers alongside privacy and access-control concerns.

#### Core Ideas

The measurement study passively captures traffic from more than 200 homes to characterize smart-device volume, timing, endpoints, encryption, and third-party dependencies.

#### Why It Matters and Impact

It reveals that an apparently fragmented IoT ecosystem is centrally dependent on a small set of cloud and DNS providers, with privacy and policy gaps.

#### Key Formulas or Algorithms

Aggregate flows by device, destination, protocol, and time; compare diurnal volume patterns and identify plaintext application traffic and tracking endpoints.

#### Intuition

Passive monitors group encrypted and plaintext flows by household device, destination, protocol, time, and byte volume, then compare patterns across more than 200 homes. Even without payload inspection, recurring contacts reveal cloud, DNS, and tracker dependencies; the measurement exposes privacy and availability risks because a small set of third parties can observe or disrupt many seemingly independent devices.

#### Main Takeaway

Real-home measurements expose centralization and privacy risks that lab IoT experiments miss.

### 96. RAIZN: Redundant Array of Independent Zoned Namespaces

**Year:** 2023 | **Collection:** 70_plus_dist | [Source](https://huaicheng.github.io/p/asplos23-razin.pdf) | [Local paper](70_plus_dist/059-raizn-redundant-array-of-independent-zoned-namespaces-2023.pdf)

#### Research Snapshot

RAIZN builds a redundant array from zoned-namespace SSDs while preserving their sequential-write rules. It stripes data and parity, logs partial-stripe updates, and manages metadata and zone resets to provide stable performance without conventional SSD garbage-collection interference.

#### Core Ideas

RAIZN exposes a zoned namespace over an array of ZNS SSDs, striping data and parity while managing sequential writes and partial stripes without device overwrites.

#### Why It Matters and Impact

It avoids unpredictable SSD garbage collection and supplies RAID-like reliability with stable throughput and lower tail latency.

#### Key Formulas or Algorithms

For a stripe, parity $P=D_1\oplus\cdots\oplus D_k$ reconstructs one failed chunk. Log partial-stripe updates in zones, persist metadata, and reset zones only after valid data relocation.

#### Intuition

RAIZN maps logical data into sequentially written zones across several drives, writes data stripes with XOR parity, and records partial-stripe updates in a log so crashes do not leave ambiguous parity. During garbage collection it copies live data before resetting a zone; respecting the append-only write pointer avoids hidden device garbage collection while parity reconstructs a chunk after one drive failure.

#### Main Takeaway

Zoned devices need array designs that respect sequential-write semantics while retaining parity protection.

### 97. Disaggregated RAID Storage in Modern Datacenters

**Year:** 2023 | **Collection:** 70_plus_dist | [Source](https://kyleshu.github.io/assets/pdf/asplos23_dRAID_paper.pdf) | [Local paper](70_plus_dist/060-disaggregated-raid-storage-in-modern-datacenters-2023.pdf)

#### Research Snapshot

dRAID brings RAID to disaggregated storage while reducing network bottlenecks. It uses peer-to-peer data exchange, nonblocking multi-stage writes, pipelined I/O, and bandwidth-aware reconstruction to balance normal and degraded operation.

#### Core Ideas

dRAID distributes RAID across networked storage nodes and uses peer-to-peer data access, nonblocking multi-stage writes, pipelines, and bandwidth-aware reconstruction.

#### Why It Matters and Impact

Remote RAID otherwise consumes NIC bandwidth for parity and recovery. dRAID approaches optimal throughput in normal and degraded operation.

#### Key Formulas or Algorithms

Pipeline read, encode, and write stages; during reconstruction choose helpers to minimize $\max_i\{	ext{load}_i/	ext{bandwidth}_i\}$ rather than reading blindly through one coordinator.

#### Intuition

For normal writes, dRAID pipelines reads, parity encoding, and writes so storage nodes exchange necessary fragments directly instead of funneling all bytes through one coordinator. When a node fails, the controller selects helpers and schedules reconstruction according to their NIC bandwidth, minimizing the slowest transfer; this keeps redundancy but avoids turning remote RAID traffic into a central network bottleneck.

#### Main Takeaway

Peer-aware pipelines and reconstruction are essential for efficient disaggregated RAID.

### 98. How (and How Not) to Write a Good SOSP Paper

**Year:** 1983 | **Collection:** 70_plus_dist | [Source](https://web.eecs.umich.edu/~prabal/teaching/eecs582-w12/readings/levin83writing.pdf) | [Local paper](70_plus_dist/061-how-and-how-not-to-write-a-good-sosp-paper-1983.pdf)

#### Research Snapshot

Based on SOSP review experience, this paper identifies recurring reasons systems papers fail: an unclear problem or contribution, weak motivation, unsupported claims, missing comparisons, and inadequate evaluation. It frames a good paper as a precise argument backed by evidence.

#### Core Ideas

The paper distills recurring SOSP review failures: unclear problem statements, weak motivation, missing comparisons, implausible claims, and inadequate evaluation.

#### Why It Matters and Impact

Its reviewer-derived advice remains influential because it connects publication quality to clear systems reasoning and evidence, not stylistic polish alone.

#### Key Formulas or Algorithms

The implicit procedure is: state the problem and contribution, explain mechanism and assumptions, compare alternatives, and test claims with measurements that isolate causes.

#### Intuition

Start with a concrete systems problem and a falsifiable contribution, then explain the mechanism and assumptions needed for it to work. Evaluate it against credible alternatives using measurements that isolate claimed causes, including limitations and negative results; this sequence lets reviewers distinguish a real, generalizable improvement from an implementation anecdote or unsupported performance claim.

#### Main Takeaway

Good papers make a precise, supported claim that survives comparison with credible alternatives.

### 99. SECRECY: Secure Collaborative Analytics in Untrusted Clouds

**Year:** 2023 | **Collection:** 70_plus_dist | [Source](https://www.usenix.org/system/files/nsdi23-liagouris.pdf) | [Local paper](70_plus_dist/062-secrecy-secure-collaborative-analytics-in-untrusted-clouds-2023.pdf)

#### Research Snapshot

SECRECY supports collaborative cloud analytics in which data owners keep their inputs hidden even from the cloud. It co-designs database planning with secure multi-party computation costs, using logical and physical optimizations to reduce secure computation, communication, and storage.

#### Core Ideas

SECRECY co-designs secure multi-party computation with a database query engine, exposing cryptographic costs to both logical and physical optimization.

#### Why It Matters and Impact

It enables jointly analyzing siloed data in untrusted clouds while improving complex query performance by orders of magnitude.

#### Key Formulas or Algorithms

Secret-share values so $x=\sum_i x_i\pmod q$; compile operators to MPC protocols, batch communication, and choose plans that minimize secure comparisons, multiplications, and rounds.

#### Intuition

Each owner splits sensitive values into cryptographic shares whose individual pieces reveal nothing, and cloud workers execute joins, filters, and aggregates through MPC protocols over those shares. SECRECY's optimizer chooses join order, partitioning, batching, and physical operators based on secure comparison, multiplication, bandwidth, and round costs, so the result is revealed only as authorized while avoiding plans that are cheap in plaintext but prohibitive under MPC.

#### Main Takeaway

Practical private analytics requires query optimization that understands MPC's computation and communication costs.

### 100. GEMINI: Fast Failure Recovery in Distributed Training with In-Memory Checkpoints

**Year:** 2023 | **Collection:** 70_plus_dist | [Source](https://assets.amazon.science/29/31/6523473f48e4af52252bac56ef51/gemini-fast-failure-recovery-in-distributed-training-with-in-memory-checkpoints.pdf) | [Local paper](70_plus_dist/063-gemini-fast-failure-recovery-in-distributed-training-with-in-memory-checkpoints-2023.pdf)

#### Research Snapshot

GEMINI checkpoints distributed training state in host CPU memory rather than remote storage. It chooses placements that retain recoverable copies under failures and schedules checkpoint traffic to avoid interfering with training communication.

#### Core Ideas

GEMINI stores distributed-training checkpoints in aggregated host CPU memory, places copies to survive failures, and schedules checkpoint traffic around training communication.

#### Why It Matters and Impact

Remote-storage checkpoints recover slowly; in-memory checkpoints offer much higher aggregate bandwidth but need placement and interference control.

#### Key Formulas or Algorithms

Choose placements maximizing recovery probability $P(\exists\ 	ext{surviving checkpoint})$ under failure models; schedule checkpoint flow in network slack to minimize its impact on training throughput.

#### Intuition

Workers periodically copy model and optimizer shards into spare host memory on carefully chosen peers rather than remote storage, while GEMINI tracks which failure domains would destroy each set of copies. It schedules that traffic around training communication and, after a failure, reconstructs state from surviving in-memory copies; the system trades volatile-memory redundancy and placement complexity for much faster restart.

#### Main Takeaway

Memory-resident, failure-aware checkpoints can greatly accelerate training recovery when network contention is controlled.

### 101. Carbink: Fault-Tolerant Far Memory

**Year:** 2022 | **Collection:** 70_plus_dist | [Source](https://www.usenix.org/system/files/osdi22-zhou-yang.pdf) | [Local paper](70_plus_dist/064-carbink-fault-tolerant-far-memory-2022.pdf)

#### Research Snapshot

Carbink provides fault-tolerant far memory using erasure coding, remote-memory compaction, one-sided RDMA, and offloaded parity computation. It aims to retain remote-memory transparency while reducing replication overhead and tail latency under machine failures.

#### Core Ideas

Carbink provides fault-tolerant far memory through erasure coding, remote-memory compaction, one-sided RMA, and offloadable parity computation.

#### Why It Matters and Impact

It improves tail latency and performance over replicated far-memory designs while using storage-efficient redundancy.

#### Key Formulas or Algorithms

An $(k,m)$ erasure code stores $k$ data and $m$ parity fragments and recovers from up to $m$ losses; compaction groups fragments and one-sided RDMA reads avoid remote CPU involvement.

#### Intuition

Carbink encodes a remote-memory object into $k$ data and $m$ parity fragments, places them across failure domains, and uses one-sided RDMA to access fragments without waking remote CPUs. Compaction groups fragment layout and offloaded parity work limits tail overhead; when up to $m$ machines fail, enough surviving fragments reconstruct the object, using less capacity than full replication at the cost of coding work.

#### Main Takeaway

Erasure coding plus efficient remote-memory management makes far memory more practical under failures.

### 102. When Idling Is Ideal: Optimizing Tail Latency for Heavy-Tailed Datacenter Workloads with Perséphone

**Year:** 2021 | **Collection:** 70_plus_dist | [Source](https://www.cis.upenn.edu/~linhphan/papers/sosp21-persephone.pdf) | [Local paper](70_plus_dist/065-when-idling-is-ideal-optimizing-tail-latency-for-heavy-tailed-datacenter-2021.pdf)

#### Research Snapshot

Perséphone is a kernel-bypass scheduler for heavy-tailed microsecond workloads. Its DARC policy reserves cores for predicted short requests and deliberately leaves those cores idle when needed, preventing long work from dominating tail latency.

#### Core Ideas

Perséphone's DARC scheduler profiles request service times and reserves cores for short requests, deliberately leaving them idle when no short work is waiting.

#### Why It Matters and Impact

For heavy-tailed microsecond workloads, work conservation lets long requests block short ones. Strategic idling lowers tail latency at higher effective utilization.

#### Key Formulas or Algorithms

Classify jobs by predicted service time; reserve $r$ cores for short jobs and dispatch long jobs elsewhere. Optimize tail objective $P(T>t)$ rather than mean utilization alone.

#### Intuition

Perséphone predicts whether queued requests are short or long and reserves selected cores for the short class; if no short request exists, it may deliberately leave those cores idle instead of starting long work. When a short request arrives, it bypasses a long one that could otherwise dominate its response time, reducing tail latency even though instantaneous utilization looks lower.

#### Main Takeaway

A little intentional idleness can reduce tail latency and total core demand for heavy-tailed workloads.

### 103. The SNOW Theorem and Latency-Optimal Read-Only Transactions

**Year:** 2016 | **Collection:** 70_plus_dist | [Source](https://www.usenix.org/system/files/conference/osdi16/osdi16-lu.pdf) | [Local paper](70_plus_dist/066-the-snow-theorem-and-latency-optimal-read-only-transactions-2016.pdf)

#### Research Snapshot

The SNOW theorem proves that a sharded read-only transaction cannot simultaneously provide strict serializability, nonblocking reads, one-version reads, and one-round reads. The result identifies a fundamental consistency-latency trade-off and guides designs for COPS and Rococo.

#### Core Ideas

The SNOW theorem proves that no read-only transaction protocol simultaneously provides strict serializability, nonblocking reads, one-version reads, and one-round reads in a sharded store.

#### Why It Matters and Impact

It establishes a hard latency-consistency boundary and guides COPS and Rococo read-only protocol designs.

#### Key Formulas or Algorithms

SNOW denotes Strict serializability, Nonblocking reads, One-version reads, and one-round trip reads. Any protocol providing the strongest transactional power must relax at least one property.

#### Intuition

A read-only transaction sends one request to each shard and would like each shard to reply immediately with one version in one round, while concurrent writers update different shards. Strict serializability requires the replies form a snapshot at a legal real-time point, but independent immediate replies can mix before and after a write; therefore a design must add waiting or coordination, return multiple versions, or use more communication.

#### Main Takeaway

Latency-optimal read-only transactions face a fundamental trade-off with strong cross-shard consistency.

### 104. Exploiting Virtual Synchrony in Distributed Systems

**Year:** 1987 | **Collection:** 70_plus_dist | [Source](https://www.cs.cornell.edu/home/rvr/sys/p123-birman.pdf) | [Local paper](70_plus_dist/067-exploiting-virtual-synchrony-in-distributed-systems-1987.pdf)

#### Research Snapshot

Virtual synchrony organizes processes into groups whose multicast deliveries and membership changes occur in consistent views. Applications can reason as if view changes are atomic, although the implementation executes work concurrently and handles failures.

#### Core Ideas

Virtual synchrony structures processes into groups where multicast delivery and membership changes appear in consistent, synchronous views.

#### Why It Matters and Impact

It lets programmers reason as if group events occur atomically while implementations execute concurrently, simplifying fault-tolerant replicated applications.

#### Key Formulas or Algorithms

Install membership view $V_k$ only after surviving members agree on delivered messages from $V_{k-1}$; ordered multicast preserves the same delivery sequence within each view.

#### Intuition

Members multicast within a numbered view and deliver messages in the view's agreed order; when failure or join detection triggers a membership change, survivors first flush or agree on the old-view deliveries. Only then do they install the next view, making the transition appear atomic to the application and ensuring surviving replicas start the new membership with the same state.

#### Main Takeaway

Consistent membership views turn failure-prone group communication into a manageable programming abstraction.

### 105. Totem: A Fault-Tolerant Multicast Group Communication System

**Year:** 1996 | **Collection:** 70_plus_dist | [Source](https://dl.acm.org/doi/pdf/10.1145/227210.227226) | [Local paper](70_plus_dist/068-totem-a-fault-tolerant-multicast-group-communication-system-1996.pdf)

#### Research Snapshot

Totem provides reliable totally ordered multicast and membership management for LAN groups. A token-based ordering protocol and recovery mechanisms make every surviving member deliver operations in the same sequence.

#### Core Ideas

Totem provides reliable totally ordered multicast over LANs using token-passing ordering, membership protocols, and recovery mechanisms.

#### Why It Matters and Impact

A common operation order keeps replicas consistent and supports real-time fault-tolerant applications while exploiting LAN broadcast performance.

#### Key Formulas or Algorithms

A circulating token grants send order; receivers deliver messages by sequence number and use membership agreement to install a new configuration after faults.

#### Intuition

A circulating token carries the next sequence number and grants its holder the right to multicast ordered messages; receivers retain and deliver messages in token order. If a token or member is lost, the membership protocol collects recovery information, agrees on a new configuration, and resumes with a consistent sequence, providing reliable total order rather than letting each receiver infer its own order.

#### Main Takeaway

Ordered multicast and membership management provide a practical substrate for consistent replicated services.

### 106. Practical Byzantine Fault Tolerance

**Year:** 1999 | **Collection:** 70_plus_dist | [Source](https://courses.cs.vt.edu/~cs5204/fall05-gback/papers/castro-osdi99.pdf) | [Local paper](70_plus_dist/069-practical-byzantine-fault-tolerance-1999.pdf)

#### Research Snapshot

PBFT replicates a state machine in an asynchronous network with Byzantine faults using pre-prepare, prepare, commit, checkpoint, and view-change phases. Authenticated quorums, batching, and a primary-backup structure make the protocol practical at $3f+1$ replicas.

#### Core Ideas

PBFT replicates a state machine with a primary and backup replicas, using pre-prepare, prepare, commit, checkpoint, and view-change phases in an asynchronous network.

#### Why It Matters and Impact

It made Byzantine replication practical enough for an NFS service with modest overhead, shifting BFT from theory toward deployment.

#### Key Formulas or Algorithms

With $n=3f+1$, a primary proposes; replicas collect $2f+1$ matching prepare and commit evidence before execution. Checkpoints stabilize history; view change replaces a faulty primary.

#### Intuition

The primary assigns a sequence number in `pre-prepare`; backups validate it, broadcast `prepare`, then broadcast `commit` after enough matching prepares. A replica executes only after a $2f+1$-sized authenticated quorum makes the request committed, checkpoints stable prefixes, and changes view when the primary stalls or misbehaves; overlapping quorums make conflicting committed histories impossible with $3f+1$ replicas.

#### Main Takeaway

BFT can be practical when quorums, batching, authenticators, and view changes are engineered together.

### 107. How (and How Not) to Write a Good SOSP Paper

**Year:** 1983 | **Collection:** 70_plus_dist | [Source](https://web.eecs.umich.edu/~prabal/teaching/eecs582-w12/readings/levin83writing.pdf) | [Local paper](70_plus_dist/070-how-and-how-not-to-write-a-good-sosp-paper-1983.pdf)

#### Research Snapshot

Based on SOSP review experience, this duplicate entry identifies recurring reasons systems papers fail: an unclear problem or contribution, weak motivation, unsupported claims, missing comparisons, and inadequate evaluation. It frames a good paper as a precise argument backed by evidence.

#### Core Ideas

This duplicate copy presents the same SOSP-submission evaluation and its concrete advice on novelty, clarity, evidence, and honest comparison.

#### Why It Matters and Impact

Its inclusion reinforces that systems contributions are judged by a coherent argument and empirical support, not implementation complexity alone.

#### Key Formulas or Algorithms

Structure the argument as problem $\rightarrow$ contribution $\rightarrow$ design $\rightarrow$ evaluation; every claimed benefit needs a baseline and a measurement that controls confounders.

#### Intuition

As with the earlier duplicate, the paper asks authors to turn an implementation into a defensible argument: define the problem and contribution, describe assumptions and mechanism, compare relevant alternatives, and measure the claimed effects. Reviewers use this chain to test novelty and evidence, so complexity alone cannot substitute for a clear, controlled evaluation.

#### Main Takeaway

A successful systems paper states one believable contribution and demonstrates it rigorously.

### 108. The Demikernel Datapath OS Architecture for Microsecond-Scale Datacenter Systems

**Year:** 2021 | **Collection:** 70_plus_dist | [Source](https://irenezhang.net/papers/demikernel-sosp21.pdf) | [Local paper](70_plus_dist/071-the-demikernel-datapath-os-architecture-for-microsecond-scale-datacenter-systems-2021.pdf)

#### Research Snapshot

Demikernel defines a narrow asynchronous datapath-OS interface for microsecond-scale systems using heterogeneous kernel-bypass devices. Its LibOS implementations map common queue operations to device-specific fast paths while allowing applications to remain portable.

#### Core Ideas

Demikernel provides a flexible datapath OS interface for heterogeneous kernel-bypass devices, implemented by prototype OSes with nanosecond-scale overhead.

#### Why It Matters and Impact

It fills the gap between application-specific bypass libraries and traditional kernels for microsecond datacenter systems, easing device portability.

#### Key Formulas or Algorithms

Applications use asynchronous queue operations such as push, pop, and wait; a LibOS maps them to device-specific datapaths while preserving the same API across hardware.

#### Intuition

An application submits asynchronous operations through a small queue-based interface, receives completion handles, and waits only when its dependency requires a result. The selected Demikernel LibOS maps those abstract operations onto the available kernel-bypass NIC or storage device and schedules device queues directly, preserving application portability while avoiding the traditional kernel's per-operation datapath overhead.

#### Main Takeaway

A narrow asynchronous datapath interface can deliver kernel-bypass speed without sacrificing portability.

### 109. Twine: A Unified Cluster Management System for Shared Infrastructure

**Year:** 2020 | **Collection:** 70_plus_dist | [Source](https://www.usenix.org/system/files/osdi20-tang.pdf) | [Local paper](70_plus_dist/072-twine-a-unified-cluster-management-system-for-shared-infrastructure-2020.pdf)

#### Research Snapshot

Twine is Facebook’s unified cluster manager for shared infrastructure. One regional control plane manages a very large fleet, while TaskControl APIs, host profiles, and autoscaling let workloads retain lifecycle and host-level customization as capacity moves across clusters.

#### Core Ideas

Twine manages shared Facebook infrastructure through one regional control plane, workload-aware TaskControl APIs, host profiles, and autoscaling on fungible small machines.

#### Why It Matters and Impact

It demonstrates that a million-machine shared fleet can replace siloed clusters while still supporting workload-specific lifecycle and host tuning needs.

#### Key Formulas or Algorithms

The controller maps jobs to hosts subject to resource and profile constraints, coordinates lifecycle actions through TaskControl, and moves capacity across clusters as demand changes.

#### Intuition

One regional control plane pools many clusters of small fungible machines and allocates them across workloads as demand changes, while each workload provides TaskControl lifecycle hooks and host profiles describing its nonstandard needs. Twine uses those interfaces during placement, scaling, and maintenance, so it can reclaim the efficiency of shared capacity without forcing every tenant into one fixed deployment or lifecycle model.

#### Main Takeaway

Unified control and explicit workload collaboration can make shared infrastructure scalable, efficient, and customizable.
