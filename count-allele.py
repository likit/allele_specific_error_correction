import sys
from collections import namedtuple

SnpObj = namedtuple("SnpObj", ["id", "ref", "ksnp", "csnp", "info"])


def parse_snps(snpfile):
    for line in snpfile:
        cols = line.split()
        snpid = cols[2]
        ref = cols[3]
        ksnp = cols[4]  # known snp
        csnp = cols[12]  # called snp
        info = cols[16]
        if csnp == ".":
            continue
        yield SnpObj(snpid, ref, ksnp, csnp, info)


def count(snp):
    infos = snp.info.split(";")
    coverage = int(infos[0].split("=")[1])
    if coverage < 10:
        yield None
    ref1, ref2, snp1, snp2 = infos[4].split("=")[1].split(",")
    ref_count = int(ref1) + int(ref2)
    snp_count = int(snp1) + int(snp2)
    return id, ref_count, snp_count


def main():
    try:
        snpfile = open(sys.argv[1])
    except IOError:
        print >> sys.stderr, "Cannot open %s, please check." % sys.argv[2]
        raise SystemExit

    for snp in parse_snps(snpfile):
        id, ref_count, snp_count = count(snp)
        print "%s\t%.4f" % (id, float(ref_count/snp_count))


if __name__=='__main__':
    main()

