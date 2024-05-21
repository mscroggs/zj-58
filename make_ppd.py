with open("zj80-in.ppd") as f:
    print(f.read().strip())

sizes = list(range(10, 3200, 10))
default = 250
assert default in sizes

def to_pt(mm):
    return int(mm * 2.83465 + 0.5)

print("*OpenUI *PageSize/Media Size: PickOne")
print("*OrderDependency: 10 AnySetup *PageSize")
print(f"*DefaultPageSize: X{default}mm")
for s in sizes:
    print(f"*PageSize X{s}mm/80mm x {s}mm: \"<</PageSize[226 {to_pt(s)}]>>setpagedevice\"")
print("*CloseUI: *PageSize")

print("*OpenUI *PageRegion/Media Size: PickOne")
print("*OrderDependency: 10 AnySetup *PageRegion")
print(f"*DefaultPageRegion: X{default}mm")
for s in sizes:
    print(f"*PageRegion X{s}mm/80mm x {s}mm: \"<</PageSize[226 {to_pt(s)}]>>setpagedevice\"")
print("*CloseUI: *PageRegion")

print(f"*DefaultImageableArea: X{default}mm")
for s in sizes:
    print(f"*ImageableArea X{s}mm/80mm x {s}mm: \"14 0 212 {to_pt(s)}\"")

print(f"*DefaultPaperDimension: X{default}mm")
for s in sizes:
    print(f"*PaperDimension X{s}mm/80mm x {to_pt(s)}mm: \"226 {to_pt(s)}\"")
print("*MaxMediaWidth: \"226\"")
print(f"*MaxMediaHeight: \"{max(sizes) + 100}\"")
print("*HWMargins: 14 0 14 0")


with open("zj80-out.ppd") as f:
    print(f.read().strip())
