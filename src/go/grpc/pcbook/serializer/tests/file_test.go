package serializer_test

import (
	"testing"

	"github.com/stretchr/testify/require"
	"google.golang.org/protobuf/proto"

	"github.com/sfortson/random-scripts/src/go/grpc/pcbook/sample"
	"github.com/sfortson/random-scripts/src/go/grpc/pcbook/serializer"

	pb "github.com/sfortson/random-scripts/go/grpc/pcbook/proto"
)

func TestFileSerializer(t *testing.T) {
	t.Parallel()

	binaryFile := "/tmp/laptop.bin"

	laptop1 := sample.NewLaptop()
	err := serializer.WriteProtobufToBinaryFile(laptop1, binaryFile)
	require.NoError(t, err)

	laptop2 := &pb.Laptop{}
	err = serializer.ReadProtobufFromBinaryFile(binaryFile, laptop2)
	require.NoError(t, err)

	require.True(t, proto.Equal(laptop1, laptop2))
}
