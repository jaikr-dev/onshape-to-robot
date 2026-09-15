import fnmatch

from .config import Config
from .message import info
from .processor import Processor
from .robot import Robot


class ProcessorRemoveLinks(Processor):
    """
    Remove links processor.
    Drops the links listed in the "remove_links" config entry, together with
    any joint or camera attached to them. Link names are the exported link
    names and may contain wildcards.
    """

    def __init__(self, config: Config):
        super().__init__(config)

        self.remove_links: list[str] = config.get("remove_links", [])

    def should_remove(self, link_name: str) -> bool:
        for entry in self.remove_links:
            if fnmatch.fnmatch(link_name, entry):
                return True
        return False

    def process(self, robot: Robot):
        if not self.remove_links:
            return

        removed = [link for link in robot.links if self.should_remove(link.name)]
        if not removed:
            print(info(f"No link matched remove_links ({self.remove_links})"))
            return

        removed_names = {link.name for link in removed}
        print(info(f"Removing links: {sorted(removed_names)}"))

        robot.links = [link for link in robot.links if link not in removed]
        robot.base_links = [
            link for link in robot.base_links if link not in removed
        ]
        robot.joints = [
            joint
            for joint in robot.joints
            if joint.parent not in removed and joint.child not in removed
        ]
        robot.cameras = [
            camera for camera in robot.cameras if camera.link_name not in removed_names
        ]
