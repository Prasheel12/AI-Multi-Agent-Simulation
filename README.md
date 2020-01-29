# Design and Implementation of a Multi-Agent Game

### Description:

1. Environment: a 1 m x 1 m field.

2. Five agents (A,B,C,D,E) can move up and down and left and right, one centimeter in every step.

3. Assume the agents have unlimited power supply.

4. For each agent, there are five targets to collect. For example for agent A the targets are TA1 to TA5.

5. Whenever a relevant target (for example TA3) is reachable by its related agent, the object is considered as collected and will disappear from the field.

6. All targets and agents are randomly scattered all over the field. Agents do not have any information about the location of none of the targets and other agents.

7. Agents have location sensor (x,y) to locate itself.

8. Agents have been given (x1,y1) and (x2,y2) so they can identify the border of the domain.

9. Agents never run out of fuel.

10. Every agent has a Radar to sense targets or other agents. The Radar can sense the type (which agent belongs to) and locate every target or agent in 10 centimeter radius. Whenever an agent locates a target (or an agent), it will receive the coordinates (x,y) of the target (or agent).

11. A target (or agent) is reachable by an agent if it falls into its Radar range (10cm).

12. Every agent has two communication channels: First is a public channel for broadcasting. In broadcast mode, the message sent by an agent will be received by all other agents. Second, a private channel to send private messages to a specific agent.

13. In both channels, agents can send any type of message but a mandatory message will be sent in broadcast mode by an agent that collected its all targets.

14. Agents avoid colliding each other. They will never remain reachable by other agents.

#### Behaviour of agents depend on the following scenarios:

##### Scenario 1: Competition

1. The game will be over as soon as one of the agents collects all its targets.

2. Only public communication channel is open for all agents. The private channels are closed. Agents can broadcast anything including right or wrong information about the location of other targets.

##### Scenario 2: Collaboration

1. The game is not over until all agents collect their own targets.

2. Both public and private channels are open. Example of a private communication: Agent Allocates TB1. It may or may not notify the agent B the location of TB1.

##### Scenario 3: Compassionate agents

1. The game will be over as soon as one of the agents collects all its targets.

2. Both public and private channels are open. Example of a private communication: Agent Allocates target TB1. It may or may not notify the agent B the location of TB1.
