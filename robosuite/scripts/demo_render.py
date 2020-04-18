"""
Test script.
"""
import imageio
import numpy as np

import robosuite
import robosuite.utils.transform_utils as T

NUM_RENDERS = 2 # 2

if __name__ == "__main__":

    # envs
    env_name_1 = "SawyerLift"
    env_name_2 = "SawyerStack"

    # controller
    controller = "EE_POS"

    # camera to render from first env
    test_camera_name = 'agentview'

    # path to output video
    video_rollout_path = "./test_demo_{}.mp4".format(0)

    controller_config = {'control_delta': True,
                           'damping': 1,
                           'force_control': False,
                           'input_max': 1,
                           'input_min': -1,
                           'interpolation': None,
                           'kp': 150,
                           'orientation_limits': None,
                           'output_max': [0.05, 0.05, 0.05, 0.5, 0.5, 0.5],
                           'output_min': [-0.05, -0.05, -0.05, -0.5, -0.5, -0.5],
                           'position_limits': None,
                           'ramp_ratio': 0.2,
                           'type': 'EE_POS_ORI',
                           'uncouple_pos_ori': True}

    env = robosuite.make(
        env_name_1,
        controller_config=controller_config,
        has_renderer=False,
        has_offscreen_renderer=True,
        use_camera_obs=False,
        control_freq=20,
        camera_height=128,
        camera_width=128,
    )
    env2 = robosuite.make(
        env_name_2,
        controller_config=controller_config,
        has_renderer=False,
        has_offscreen_renderer=True,
        use_camera_obs=True,
        control_freq=20,
        camera_height=512,
        camera_width=512,
        camera_name='agentview',
    )

    env.reset()
    env2.reset()

    video_writer = imageio.get_writer(video_rollout_path, fps=20)
    video_skip = 5
    video_count = 0

    low, high = env.action_spec
    for step in range(200):

        # step each env with a random action
        action = np.random.uniform(low, high)
        env.step(action)
        env2.step(action)

        # render video for first env
        if video_count % video_skip == 0:
            for _ in range(NUM_RENDERS):
                video_img = env.sim.render(
                    height=512,
                    width=512,
                    camera_name=test_camera_name,
                )[::-1]
            video_writer.append_data(video_img)
        video_count += 1
