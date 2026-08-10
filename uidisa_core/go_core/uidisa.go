package main

import (
	"crypto/rand"
	"crypto/sha256"
	"errors"
	"fmt"
	"time"
)

// IntentVector defines Goal x Context x Boundary rules
type IntentVector struct {
	Goal        string
	ContextHash string
	Boundaries  []string
}

// SmartInformationUnit (SIU) Packet
type SmartInformationUnit struct {
	SemanticWeight   float64
	ContextSignature string
	EntropyDelta     int
	PayloadTensor    []byte
	InternalKey      []byte
	CreatedAt        int64
}

// NewSIU creates an active self-defending unit
func NewSIU(payload []byte, weight float64, contextHash string) (*SmartInformationUnit, error) {
	if weight < 0.0 || weight > 1.0 {
		return nil, errors.New("semantic weight must be between 0.0 and 1.0")
	}

	key := make([]byte, 32)
	rand.Read(key)

	siu := &SmartInformationUnit{
		SemanticWeight:   weight,
		ContextSignature: contextHash,
		EntropyDelta:     0,
		InternalKey:      key,
		CreatedAt:        time.Now().Unix(),
	}

	siu.PayloadTensor = siu.scramble(payload, key)
	return siu, nil
}

func (s *SmartInformationUnit) scramble(data, key []byte) []byte {
	hash := sha256.Sum256(key)
	scrambled := make([]byte, len(data))
	for i := 0; i < len(data); i++ {
		scrambled[i] = data[i] ^ hash[i%len(hash)]
	}
	return scrambled
}

// TriggerSelfDestruct immediately overwrites payload and key with noise
func (s *SmartInformationUnit) TriggerSelfDestruct() {
	s.EntropyDelta = 1
	noise := make([]byte, len(s.PayloadTensor))
	rand.Read(noise)

	for i := 0; i < len(s.PayloadTensor); i++ {
		s.PayloadTensor[i] = s.PayloadTensor[i] ^ noise[i]
	}
	rand.Read(s.InternalKey) // Destroy key
}

func main() {
	fmt.Println("=== UIDISA Go Core Engine Initiated ===")
	validHash := "8f434346648f6b96df89dda901c5176b10a6d83961dd3c1ac88b59b2dc327aa4"

	siu, _ := NewSIU([]byte("CRITICAL_ADAS_SPEED_CONTROL"), 0.99, validHash)
	fmt.Printf("SIU Package Created. Payload Tensor Size: %d bytes\n", len(siu.PayloadTensor))

	// Simulate Attack -> Self Destruct
	siu.TriggerSelfDestruct()
	fmt.Println("🚨 Anomaly Triggered: Payload Irreversibly Destructed in Memory.")
}
