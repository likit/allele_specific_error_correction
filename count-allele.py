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
        info = cols[15]
        if csnp == ".":
            continue
        yield SnpObj(snpid, ref, ksnp, csnp, info)


def count(snp):
    infos = snp.info.split(";")
    coverage = int(infos[0].split("=")[1])
    if coverage < 10:
        return None

    ref_count = 0
    snp_count = 0
    for i in infos:
        if "DP4" in i:
            ref1, ref2, snp1, snp2 = i.split("=")[1].split(",")
            ref_count = int(ref1) + int(ref2)
            snp_count = int(snp1) + int(snp2)

    if (ref_count == 0 and snp_count == 0):
        raise ValueError, "No reads mapped to this position."

    return id, ref_count, snp_count, coverage


def main():
    try:
        snpfile = open(sys.argv[1])
    except IOError:
        print >> sys.stderr, "Cannot open %s, please check." % sys.argv[2]
        raise SystemExit

    for snp in parse_snps(snpfile):
        try:
            id, ref_count, snp_count, coverage = count(snp)
        except TypeError:
            pass
        else:
            if (snp_count == 0 or ref_count == 0):
                continue
            else:
                print "%s\t%d\t%.4f" % (snp.id,
                                        coverage,
                                        float(ref_count)/snp_count,
                                        )


if __name__=='__main__':
    main()

