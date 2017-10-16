class SoHDD:
	def actions(self):
		import os
		disk = os.statvfs("/home")
		capacity = disk.f_bsize * disk.f_blocks
		available = disk.f_bsize * disk.f_bavail
		used = disk.f_bsize * (disk.f_blocks - disk.f_bavail)
		print used, available, capacity
		print used / 1024, available / 1024, capacity / 1024
		print used / 1.048576e6, available / 1.048576e6, capacity / 1.048576e6
		print used / 1.073741824e9, available / 1.073741824e9, capacity / 1.073741824e9
		return []
