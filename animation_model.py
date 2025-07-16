import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
import tempfile

# Global variables to track robot position and path
robot_pos = np.array([8.5, 5.3])
path_points = [[8.5, 5.0], [8.5, 5.3]]  # Initial path

def update_robot_position(direction):
    global robot_pos, path_points
    step = 0.2
    
    # Store previous position
    old_pos = robot_pos.copy()
    
    # Update position based on direction
    if direction == 'up':
        robot_pos[1] = min(5.8, robot_pos[1] + step)
    elif direction == 'down':
        robot_pos[1] = max(0.2, robot_pos[1] - step)
    elif direction == 'left':
        robot_pos[0] = max(0.2, robot_pos[0] - step)
    elif direction == 'right':
        robot_pos[0] = min(9.8, robot_pos[0] + step)
    
    # Add new point to path if position changed
    if not np.array_equal(old_pos, robot_pos):
        path_points.append(robot_pos.tolist())
        # Keep only last 10 path points
        if len(path_points) > 10:
            path_points.pop(0)

def generate_animation_gif():
    # Set up the figure
    plt.style.use('default')
    plt.rcParams['figure.dpi'] = 100
    fig, ax = plt.subplots(figsize=(10, 6))
    
    # Set plot dimensions
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 6)

    # Set background color
    ax.set_facecolor('#87CEEB')
    fig.patch.set_facecolor('white')

    # Add grid
    ax.grid(True, color='white', linestyle='-', linewidth=0.5, alpha=0.3)

    # Draw scrap (black square)
    scrap_pos = [8.5, 5.0]
    ax.scatter(scrap_pos[0], scrap_pos[1], c='black', marker='s', s=100, label='Scrap')

    # Draw robot (red dot)
    ax.scatter(robot_pos[0], robot_pos[1], c='red', marker='o', s=150, label='Robot')

    # Draw path (dashed red line)
    path_array = np.array(path_points)
    ax.plot(path_array[:, 0], path_array[:, 1], 'r--', linewidth=1.5, alpha=0.7, label='Path')

    # Configure axis
    ax.set_xlabel('Width', fontsize=12, labelpad=10)
    ax.set_ylabel('Height', fontsize=12, labelpad=10)
    
    # Set ticks
    ax.set_xticks(np.arange(0, 11, 2))
    ax.set_yticks(np.arange(0, 7, 1))
    ax.tick_params(colors='black', labelsize=10)

    # Add legend with white background
    legend = ax.legend(loc='upper right', framealpha=1, fontsize=10)
    legend.get_frame().set_facecolor('white')
    legend.get_frame().set_edgecolor('none')

    # Set title in all caps
    ax.set_title('WATER SURFACE CLEANING ROBOT', pad=15, fontsize=14, fontweight='bold')

    # Save the plot
    plt.tight_layout()
    tmpfile = tempfile.NamedTemporaryFile(suffix='.png', delete=False)
    plt.savefig(tmpfile.name, 
                bbox_inches='tight',
                facecolor=fig.get_facecolor(),
                edgecolor='none',
                pad_inches=0.1)
    plt.close()
    
    return tmpfile.name
